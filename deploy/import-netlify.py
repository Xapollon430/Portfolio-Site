#!/usr/bin/env python3
"""Relocate preserved Netlify publish directories under /secret. Keep originals intact."""
import json,pathlib,re,shutil,sys
source=pathlib.Path(sys.argv[1]); destination=pathlib.Path(sys.argv[2])
for project in json.loads((source/'manifest.json').read_text()):
 slug=project['slug']; old=source/slug; new=destination/slug
 if new.exists():shutil.rmtree(new)
 shutil.copytree(old,new)
 prefix='/secret/'+slug
 files={str(p.relative_to(old)).lower():str(p.relative_to(old)) for p in old.rglob('*') if p.is_file()}
 for p in new.rglob('*'):
  if p.suffix not in ['.html','.js','.css','.json','.svg']:continue
  s=p.read_text(errors='strict')
  # Netlify file names are case insensitive; Linux paths are case sensitive.
  for canonical in sorted(files.values(),key=len,reverse=True):
   s=re.sub(re.escape('/'+canonical),lambda m:prefix+'/'+canonical,s,flags=re.I)
   basename=pathlib.PurePosixPath(canonical).name
   if len(basename)>8:s=re.sub(re.escape(basename),lambda m:basename,s,flags=re.I)
  s=re.sub(r'(\.p=)[\"\']/[\"\']',lambda m:m[1]+json.dumps(prefix+'/'),s)
  if p.suffix=='.html':s=s.replace('<head>','<head><base href="'+prefix+'/">',1)
  if slug=='aftershock' and p.suffix=='.js':
   s=s.replace('function Mh(e){let{basename:t,','function Mh(e){let{basename:t="'+prefix+'",')
  p.write_text(s)
 print(slug,flush=True)

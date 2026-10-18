# Archived Netlify projects

The seven projects in netlify-projects.json are preserved at /srv/www/projects/secret on vehbi-portfolio.exe.xyz. Original published files and manifests are backed up at /home/exedev/netlify-backups. import-netlify.py converts those originals to subroute assets without changing the backup.

The older Oakwin MedLaunch dashboard was rebuilt from the exact Netlify deployed commit ccef5e2. Source changes are pushed to Oakwin-Engineering/MedLaunch branch exe-portfolio-archive, commit 179d1d5. Run npm ci and npm run build in flowbite-svelte-admin-dashboard, then deploy build/ into /srv/www/projects/secret/medlaunch-oakwin/. This replaces its original Netlify SSR runtime with static pages.

WrapPilot and Shiny remain on Netlify. Pushshift is an old client that depends on api.pushshift.io; its empty feed is an existing upstream limitation. LuxDrive email delivery was not migrated, per request.

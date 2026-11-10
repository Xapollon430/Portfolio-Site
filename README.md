# Vehbi Portfolio

Static HTML, CSS, and assets for [vehbikaraagac.com](https://vehbikaraagac.com/). Track priorities in [Linear](https://linear.app/sosa-llc/project/vehbi-portfolio-5bf5a35b4de2).

Preview the static files with `python3 -m http.server 8765 --bind 127.0.0.1` from the repo root. nginx redirects, proxied endpoints, and separately hosted demos require the VM configuration.

## Deploy to exe.dev

- VM: `vehbi-portfolio` (`vehbi-portfolio.exe.xyz`). Connect using authorized SSH: `ssh exe.dev ssh vehbi-portfolio`.
- Source checkout: `/home/exedev/portfolio-source`, branch `master`. Published static files: `/srv/www/portfolio`. nginx serves the site on port 8000. Other hosted projects use `/srv/www/projects`.
- Pushing to GitHub does not publish the site.

For an authorized portfolio-only release, check that the VM checkout is clean, fetch `origin/master`, and confirm the intended commit and changed paths. Keep a backup of the affected published files before replacing them. From the VM checkout, publish the reviewed commit using the same file list as the existing update script:

```bash
set -o pipefail
cd /home/exedev/portfolio-source
git archive "$release" index.html assets images secret Case-Study-NetDesign.pdf Jan2024-ME-Enablis-Case-Study-Final-YM.pdf | tar -x -C /srv/www/portfolio
```

Set `release` to the reviewed commit SHA before running the command. The archive overlays files; it does not remove deleted paths. Review any intended removals separately. Verify HTTPS and the changed page or asset on the custom domain; for rollback, restore the affected published files from backup and recheck.

[deploy/update.sh](deploy/update.sh) is the broader VM update: it pulls and publishes the portfolio and ClockBlocked, builds and restarts Anunnaki, and validates and reloads nginx. Use it only when those changes are in scope. See [deploy/nginx.conf](deploy/nginx.conf) for route mappings and [the archive notes](deploy/README-netlify-archive.md) for imported static projects.

# Vehbi Portfolio

- Priorities and follow-up: [Vehbi Portfolio in Linear](https://linear.app/sosa-llc/project/vehbi-portfolio-5bf5a35b4de2).
- Start with [README.md](README.md) for preview and deployment. Production is https://vehbikaraagac.com/ on exe.dev VM `vehbi-portfolio`.
- For an authorized portfolio-only release, publish the reviewed Git revision to `/srv/www/portfolio` using the README. Verify the changed content on the custom domain.
- Read [deploy/update.sh](deploy/update.sh) before using it: it updates other apps and reloads nginx. Keep unrelated routes and services outside a portfolio-only release.

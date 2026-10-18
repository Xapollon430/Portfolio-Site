#!/usr/bin/env bash
set -euo pipefail
cd /home/exedev/portfolio-source
git pull --ff-only origin master
git archive HEAD index.html assets images Case-Study-NetDesign.pdf Jan2024-ME-Enablis-Case-Study-Final-YM.pdf | tar -x -C /srv/www/portfolio
cd /home/exedev/clockblocked-source
git pull --ff-only origin main
sudo install -m 644 server/index.html server/privacy_policy.html /srv/www/projects/clockblocked/
sudo install -m 644 /home/exedev/portfolio-source/deploy/nginx.conf /etc/nginx/sites-available/default
sudo nginx -t
sudo systemctl reload nginx
printf 'Portfolio commit: '
git -C /home/exedev/portfolio-source rev-parse HEAD
printf 'ClockBlocked commit: '
git -C /home/exedev/clockblocked-source rev-parse HEAD

#!/bin/sh
# One-time (or after editing a .mmd): pre-render the four flowcharts.
#
# This exists so questions.html does NOT pull 2.8 MB of Mermaid from a CDN to draw
# four static diagrams that never change — which also made the page useless offline.
#
# mermaid-cli drives a real browser. Puppeteer's own Chrome download is not needed;
# point it at the system one instead.
cd "$(dirname "$0")" || exit 1
for i in 01 02 03 04; do
  npx -y @mermaid-js/mermaid-cli@11 \
      -i "flow-$i.mmd" -o "flow-$i.svg" \
      -b transparent -c mermaid-theme.json -p puppeteer.json || exit 1
done
ls -la ./*.svg

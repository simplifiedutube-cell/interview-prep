#!/bin/sh
# Screenshot a page at a true mobile viewport. Headless Chrome ignores --window-size
# for layout, so the page is framed in a 390px iframe instead.
#   build/dev/shot.sh /index.html /tmp/out.png [height]
D="$(cd "$(dirname "$0")/../../public" && pwd)"
PAGE="${1:-/index.html}"; OUT="${2:-/tmp/shot.png}"; H="${3:-1700}"
cat > "$D/_shot.html" <<HTML
<!DOCTYPE html><meta charset=utf-8>
<style>html,body{margin:0;background:#888}iframe{border:0;width:390px;height:${H}px;display:block}</style>
<iframe src="$PAGE"></iframe>
HTML
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --virtual-time-budget=9000 --screenshot="$OUT" --window-size=390,"$H" --hide-scrollbars \
  "http://localhost:8099/_shot.html" 2>/dev/null
rm -f "$D/_shot.html"
ls -la "$OUT"

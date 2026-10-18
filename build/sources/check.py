"""HTTP-check every distinct URL in sources.py. A dead link in a study plan is
worse than no link, so this runs before the sources are allowed into the build."""
import sys, concurrent.futures as cf, urllib.request, urllib.error
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from sources import SRC, DSA_SRC

urls = {}
for t, m in SRC.items():
    for i, s in m.items():
        if "|" in s: urls.setdefault(s.split("|", 1)[1], s.split("|", 1)[0])
urls.setdefault(DSA_SRC.split("|", 1)[1], DSA_SRC.split("|", 1)[0])

def check(u):
    req = urllib.request.Request(u, method="GET", headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        # without an Accept header some CDNs answer 406 Not Acceptable, which
        # looks exactly like a dead link and is not one
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r: return u, r.status, ""
    except urllib.error.HTTPError as e: return u, e.code, e.reason
    except Exception as e: return u, 0, type(e).__name__

with cf.ThreadPoolExecutor(12) as ex:
    res = sorted(ex.map(check, urls))
bad = [r for r in res if r[1] >= 400 or r[1] == 0]
for u, code, why in res:
    mark = "ok  " if 200 <= code < 400 else "BAD "
    print(f"  {mark}{code:<4} {urls[u][:44]:<44} {u}" + (f"  [{why}]" if why else ""))
print(f"\n  {len(res) - len(bad)}/{len(res)} reachable")
sys.exit(1 if bad else 0)

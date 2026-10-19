"""HTTP-check every URL in curriculum.py. A dead link in a study plan is worse
than no link — the whole point of the research pass was to avoid inventing them."""
import sys, concurrent.futures as cf, urllib.request, urllib.error, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from curriculum import CURRICULUM

urls = {}
for tid, rows in CURRICULUM.items():
    for r in rows:
        if r["url"]: urls.setdefault(r["url"], r["label"])

HDRS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9"}

def check(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u, headers=HDRS), timeout=30) as r:
            return u, r.status, ""
    except urllib.error.HTTPError as e: return u, e.code, e.reason
    except Exception as e: return u, 0, type(e).__name__

with cf.ThreadPoolExecutor(14) as ex:
    res = sorted(ex.map(check, urls))
bad = [r for r in res if not (200 <= r[1] < 400)]
for u, c, why in bad:
    print(f"  BAD {c:<4} {urls[u][:50]:<50} {u}" + (f"  [{why}]" if why else ""))
print(f"\n  {len(res)-len(bad)}/{len(res)} reachable")
sys.exit(1 if bad else 0)

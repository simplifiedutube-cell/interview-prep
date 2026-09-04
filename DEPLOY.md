# Deploying the prep site

GitHub → Vercel, with progress in a Turso (libSQL/SQLite) database so every device
sees the same state.

```bash
python3 build/build.py          # writes public/ ; needs pandoc (brew install pandoc)
```

Everything else is Python stdlib. Vercel runs **no build** — it serves the committed
`public/` folder and the functions in `api/`.

---

## Why the pieces are what they are

- **Vercel serverless has no persistent filesystem.** Each invocation gets a fresh,
  isolated `/tmp`, so a real `.sqlite` file cannot live there. Turso is libSQL — the
  open-source SQLite fork — reached over HTTP. Same SQL, same semantics.
- **Vercel Hobby cannot password-protect a production URL.** So `middleware.js` does it.
  It is the only thing between the open internet and the metric-defence dossier, the
  comp targets, the client architectures — and write access to your database.
- **Vercel's build image has no pandoc**, which is why `public/` is committed.

## Step 0 — rescue your current progress. Do this first.

`localStorage` is scoped to an origin, so anything ticked at the old URL is invisible at
the new one. On the device that has your real progress: **☰ → Data → Back up**, save the
JSON to iCloud Drive. Note how many keys are in `state`.

## Step 1 — build and self-check locally

```bash
python3 build/build.py
node build/dev/sql-test.mjs        # 17 checks — the sync SQL against real SQLite
node build/dev/api-test.mjs        # 21 checks — the API handlers end to end
python3 -m http.server 8099 --directory public &
cp build/dev/func.html public/_func.html        # 19 checks
cp build/dev/regress.html public/_regress.html  # 10 checks
cp build/dev/sync.html public/_sync.html        # 16 checks
# open /_func.html, /_regress.html, /_sync.html and read the results
```

The `_*.html` harnesses are wiped by the next build. They are dev tools, not part of the site.

## Step 2 — the repo

The remote is `github.com/DineshKadiam/interview-prep`. The CLI here is authenticated as a
different account, so authenticate as **DineshKadiam** first:

```bash
gh auth login                     # choose DineshKadiam
gh repo create DineshKadiam/interview-prep --private --source=. --remote=origin
# (if the repo already exists, skip create and just push)
git add -A && git commit -m "feat: Vercel + Turso sync" && git push -u origin main
```

Before pushing, confirm what is and is not going up:

```bash
git ls-files public | wc -l                      # ~48 — the built site IS committed
git ls-files | grep -E '\.env|node_modules'      # must be empty
```

> **Keep the repo private.** It contains `answers/`, the ₹ comp targets in `story-bank.md`
> and `pipeline.md`, the six client architectures, and both `.docx` résumés in source form.
> The site's passphrase gate does nothing for the repo.

## Step 3 — Vercel

1. vercel.com/new → import the repo → Framework Preset **Other**. `vercel.json` already
   pins the output directory and an empty build command.
2. **Storage → Turso** in the Vercel dashboard → create a database (free tier, no card).
   It injects `TURSO_DATABASE_URL` and `TURSO_AUTH_TOKEN` automatically.
3. **Settings → Environment Variables**, both marked *Sensitive*, all environments:

   | Name | Value |
   |---|---|
   | `APP_PASSPHRASE` | what you type to get in. **Five random words or 20+ characters** — this is the only gate |
   | `AUTH_SECRET` | `openssl rand -hex 32`. Signs the cookie; rotating it signs out every device instantly |

4. **Redeploy.** Environment variables do not apply to deployments that already exist.

The schema creates itself (`CREATE TABLE IF NOT EXISTS`) on the first API call.

## Step 4 — first login and migration

Open the URL. You get redirected to `/login.html`. Enter the passphrase.

- **Progress already on this device:** nothing to do. The first sync runs in **seed mode**,
  which can only *raise* a grade and never writes a tombstone — so if two devices each hold
  real progress, they merge to the union instead of the second one erasing the first.
- **Progress from the old origin:** ☰ → Data → **Restore** → the JSON from step 0. Confirm
  the count matches. That pushes as a normal last-write-wins sync, which is right: a restore
  means "make it look like this file", un-ticks included.

Check the drawer reads `Synced just now.`

## Step 5 — the phone

Safari → Share → **Add to Home Screen** → launch → sign in once (90 days).

Then actually test it before trusting it: tick something on the laptop, reopen on the phone,
watch it appear. Then tick on the phone and watch it appear on the laptop.

Home-screen install is still a durability requirement — iOS clears script-writable storage
after 7 idle days for sites that are not home-screened. The database means that is no longer
data loss, but you would have to sign in again.

## Redeploying

```bash
python3 build/build.py && git add -A && git commit -m "…" && git push
```

Vercel deploys in ~20s with no build step; the "New version — tap to update" pill appears on
each device.

> **The one new way to get this wrong:** `public/` is committed now, so pushing a source edit
> *without rebuilding* silently deploys the old site. Make `python3 build/build.py &&` the
> first half of the muscle memory.

## Editing content

| To change | Edit |
|---|---|
| A syllabus item, track, or the daily routine | `master-tracker.html` — the `DAY` / `TRACKS` / `DSA_LIST` constants |
| A library document | its `.md`, then rebuild |
| Which docs publish, their order and titles | `build/manifest.py` |
| Shared styling | `build/site/site.css` |
| Sync behaviour | `build/site/sync.js` (client), `api/*.js` + `lib/db.js` (server) |
| A Mermaid flowchart | `build/site/mermaid/flow-0N.mmd`, then `build/site/mermaid/render.sh` |

> ⚠️ **Never reword an existing item in `master-tracker.html`.** `idFor(track, group, text)`
> hashes the group title and item text into the storage key. Changing the wording orphans that
> item's grade both locally *and* in the database. Adding and removing whole items is fine.

## What the gate does and does not protect

**Does:** the origin, including static HTML — middleware runs before the CDN cache, so there
is no cached copy to leak. The database against writes by strangers. Preview deployments.
Search engines (`robots.txt` + `X-Robots-Tag` + `noindex`).

**Does not:** a device that has already signed in — the cached pages and localStorage are
plaintext on disk, which is the price of working offline. Use **Sign out** in the drawer if a
device leaves your hands; it clears the caches and unregisters the worker. It is also not
multi-user: anyone with the passphrase has full read and write.

Rotate `AUTH_SECRET` to invalidate every session everywhere.

## Local development against the real API

```bash
npx vercel link
npx vercel env pull .env.development.local     # gitignored — holds a live write token
npx vercel dev
```

`setCookie()` drops the `Secure` attribute when `VERCEL_ENV=development`, because Safari
refuses `Secure` cookies over `http://localhost` and login would appear to work while nothing
persisted.

The static-only loop (`python3 -m http.server 8099 --directory public`) still works and is
what the dev harnesses use. With no API reachable the sync layer queues changes and the
tracker behaves exactly as it did before — that is asserted by the 29 checks in
`func.html` + `regress.html`.

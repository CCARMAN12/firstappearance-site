# firstappearance.us

The public demo for First Appearance, served as a single static page.

Deliberately standalone: no framework, no build step, no third-party script
beyond the webfont. The page it replaced was hosted on claude.ai, which put a
sign-in wall in front of a QR code — a scan gets one chance, and a login screen
ends it.

## Deploying

Push to `main`. GitHub Pages serves it at the domain in `CNAME`.

## stats.json

The page fetches `stats.json` on load and quietly keeps its built-in numbers if
the request fails. That is the designed state, not a bug: a page whose counts
are unavailable must still be correct, never a spinner or a zero.

To make the counts live, generate the file from the nightly run and commit it:

    casewire stats --out ~/Developer/firstappearance-site/stats.json

The payload carries counts only — booked, matched, queued, mailed, refused, and
refusal reasons with tallies. It has no name, address or date of birth in it,
and a test asserts that by reading the records back out of the database.

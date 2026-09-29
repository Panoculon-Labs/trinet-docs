# Trinet Documentation

Source of **https://docs.panoculonlabs.com** — the public documentation for Trinet cameras by
Panoculon Labs: getting started, LED indications, the Trinet app, firmware releases, the Android and
iOS SDKs, the Python toolkit and calibration.

## Working on the docs

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve          # live preview at http://127.0.0.1:8000
.venv/bin/mkdocs build --strict # what CI runs
```

Ground rules:

- Describe what the camera **does**, never how it is built. No component part numbers, vendors,
  internal program names, update-protocol or security details, and no customer names.
- Every specification, LED meaning, rate or limit must match the current firmware and SDK.
  When the product changes, update the page and the release history together.
- A disclosure check runs in CI on every change (its term list is kept out of this repository).

Published with GitHub Pages from `main`.

#!/usr/bin/env bash
# Local pre-publish check: strict build + the full private disclosure scan.
# The scan's term list lives in the private Trinet-KB repo (set KB_DIR if it isn't in the default place).
set -euo pipefail
cd "$(dirname "$0")/.."
KB_DIR="${KB_DIR:-$HOME/Trinet/Trinet-KB}"

.venv/bin/mkdocs build --strict
if [ -x "$KB_DIR/.venv/bin/python" ]; then
  "$KB_DIR/.venv/bin/python" "$KB_DIR/scripts/scan_public_docs.py" docs mkdocs.yml README.md site
else
  echo "warning: $KB_DIR not found; disclosure scan skipped" >&2
fi

#!/usr/bin/env python3
from pathlib import Path
import sys

WATCH_DIRS = ["models", "evals", "risk", "src"]
REQUIRED_PATHS = [
    Path("evidence/lica_crosswalk.csv"),
    Path("schemas/incident_schema.json"),
    Path("templates/bv01_memo.md"),
]

def main():
    changed = sys.argv[1:]
    touches_governed_area = any(any(part == wd or f.startswith(wd + "/") for wd in WATCH_DIRS) for f in changed for part in [f.split("/")[0]])
    missing = [str(p) for p in REQUIRED_PATHS if not p.exists()]
    if touches_governed_area and missing:
        print("FAIL: governed change detected but required LICA artifacts are missing:")
        for m in missing:
            print(f" - {m}")
        raise SystemExit(1)
    print("PASS: LICA governance check clear.")

if __name__ == "__main__":
    main()

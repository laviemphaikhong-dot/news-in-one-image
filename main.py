#!/usr/bin/env python3
"""Publish the 18 November 2026 front page for the make.fun bounty.

``entry.png`` beside this file is the finished page. Executing the
program copies those exact bytes into the directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` when the
variable is absent). Nothing is fetched, generated or randomised at
run time, which is why two executions always produce the same file.
"""

import os
import shutil
from pathlib import Path

FRONT_PAGE = Path(__file__).resolve().parent / "entry.png"


def destination() -> Path:
    raw = os.getenv("MAKEFUN_OUTPUT_DIR")
    return Path(raw) if raw else Path("/output")


def main() -> None:
    if not FRONT_PAGE.exists():
        raise SystemExit("entry.png not found next to main.py")
    target = destination()
    target.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(FRONT_PAGE, target / "entry.png")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Dependency-free structural checks for the audited offline portfolio."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
files = ["index.html", "dashboard_v1.html", "dashboard_v2.html", "dashboard_v3.html"]
errors = []
for name in files:
    path = root / name
    if not path.is_file():
        errors.append(f"Missing: {name}")
        continue
    content = path.read_text(encoding="utf-8")
    required = ['id="v1"', 'id="v2"', 'id="v3"', 'id="sun"', 'id="b2"', 'id="scatter"']
    for marker in required:
        if marker not in content:
            errors.append(f"{name}: missing {marker}")
    if "<script src=" in content or "<link rel=\"stylesheet\"" in content:
        errors.append(f"{name}: external dependency")
    if "const V2=" not in content or ",V3=" not in content:
        errors.append(f"{name}: datasets missing")
    if content.count("budgeted_cost") < 49:
        errors.append(f"{name}: V2 source records incomplete")
    if content.count('"City":') < 10:
        errors.append(f"{name}: V3 records incomplete")
    if not re.search(r'<html[^>]+lang="pt-BR"', content):
        errors.append(f"{name}: language marker missing")
    print(f"{name}: {len(content):,} chars inspected")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("PASS: 4 standalone HTMLs structurally present. Browser testing remains required.")

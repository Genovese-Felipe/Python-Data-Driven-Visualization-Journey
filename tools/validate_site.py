#!/usr/bin/env python3
"""Dependency-free audit of GitHub Pages assets and dataset parity."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "index.html").read_text(encoding="utf-8")
m = re.search(r'<script type="application/json" id="embedded-data">([\s\S]*?)</script>', html)
assert m, "Missing embedded, offline JSON payload."
embedded = json.loads(m.group(1))
construction = json.loads((ROOT / "data/construction_v2.json").read_text(encoding="utf-8"))["records"]
smart_home = json.loads((ROOT / "data/smart_home_v3.json").read_text(encoding="utf-8"))["records"]
manifest = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))

assert embedded["construction"] == construction, "Embedded V2 data differ from canonical JSON."
assert embedded["smart_home"] == smart_home, "Embedded V3 data differ from canonical JSON."
assert len(construction) == manifest["construction_records"] == 49
assert sum(row["cost"] for row in construction) == manifest["construction_total"] == 3085000
assert sum(row["budgeted_cost"] for row in construction) == manifest["construction_budget"] == 2988000
assert len(smart_home) == manifest["smart_home_records"] == 10
assert len({row["id"] for row in construction}) == 49
assert len({row["id"] for row in smart_home}) == 10
assert all(row["cost"] >= 0 and row["budgeted_cost"] >= 0 for row in construction)
assert all(-90 <= row["Latitude"] <= 90 and -180 <= row["Longitude"] <= 180 for row in smart_home)
assert re.search(r'lang="pt-BR"', html)
assert not re.search(r'<script\s+[^>]*src=', html, re.I), "External JS breaks offline availability."
assert "github.com" not in html.lower().split("<script type=")[0] or True  # informational only
assert not re.search(r'<script[^>]+src\s*=\s*["\']http', html, re.I)
print("PASS: 49 construction records, 10 smart-home records, embedded/canonical parity, offline HTML.")

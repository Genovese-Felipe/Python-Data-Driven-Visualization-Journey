#!/usr/bin/env python3
"""Dependency-free audit of GitHub Pages assets and dataset parity."""
import json
import ast
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
assert not re.search(r'<script[^>]+src\s*=\s*["\']http', html, re.I)
# Read literal input tables from Python source WITHOUT importing or executing apps.
def literal_source_assignment(file_path, variable="data"):
    source = (ROOT / file_path).read_text(encoding="utf-8-sig")
    module = ast.parse(source, filename=file_path)
    for statement in module.body:
        if isinstance(statement, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == variable for t in statement.targets
        ):
            try:
                return ast.literal_eval(statement.value)
            except (ValueError, TypeError, SyntaxError):
                continue
    raise AssertionError(f"No literal {variable!r} data found in {file_path}")


source_v2 = literal_source_assignment("dashboards/v2_construction/V2_script.py")
source_v3 = literal_source_assignment("dashboards/v3_smart_home/Plan_V3_funcional.py")
assert construction == [
    {"id": f"C{i:03d}", **row}
    for i, row in enumerate(source_v2, start=1)
], "V2 Python records drifted from canonical JSON"
expected_smart = [
    {"id": f"S{i:03d}", **{key: values[i - 1] for key, values in source_v3.items()}}
    for i in range(1, len(source_v3["City"]) + 1)
]
assert smart_home == expected_smart, "V3 Python rows drifted from canonical JSON"
print("PASS: 49 construction records, 10 smart-home records, embedded/canonical parity, offline HTML.")

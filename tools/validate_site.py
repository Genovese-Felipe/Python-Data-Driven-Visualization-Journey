#!/usr/bin/env python3
"""Validate that main CSV sources, canonical JSON and standalone HTML agree."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
match = re.search(
    r'<script type="application/json" id="embedded-data">([\s\S]*?)</script>', HTML
)
assert match, "Offline embedded JSON missing"
embedded = json.loads(match.group(1))
canonical_construction = json.loads(
    (ROOT / "data/construction_v2.json").read_text(encoding="utf-8")
)["records"]
canonical_smart = json.loads(
    (ROOT / "data/smart_home_v3.json").read_text(encoding="utf-8")
)["records"]
manifest = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))

def csv_records(path, expected_headers):
    with (ROOT / path).open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames == expected_headers, (path, reader.fieldnames)
        rows = list(reader)
    assert rows and all(None not in r and None not in r.values() for r in rows), (
        path, "Malformed comma-separated fields"
    )
    return rows

v2_columns = ["pillar", "area", "service", "task", "sub_task", "cost", "budgeted_cost"]
v2 = csv_records("dashboards/v2_construction/data.csv", v2_columns)
reconciled_v2 = [
    {"id": f"C{i:03d}", **{
        k: int(value) if k in ("cost", "budgeted_cost") else value
        for k, value in row.items()
    }}
    for i, row in enumerate(v2, 1)
]
assert len(v2) == 49
assert reconciled_v2 == canonical_construction, "V2 CSV != JSON: audit source drift"
assert embedded["construction"] == canonical_construction, "V2 inline HTML != JSON"
assert sum(r["cost"] for r in reconciled_v2) == manifest["construction_total"] == 3085000
assert sum(r["budgeted_cost"] for r in reconciled_v2) == manifest["construction_budget"] == 2988000

v3_columns = ["Region", "City", "Installation_Type", "Installation_Cost", "Annual_Energy_Savings", "Number_of_Devices", "Customer_Satisfaction", "Latitude", "Longitude"]
v3 = csv_records("dashboards/v3_smart_home/data.csv", v3_columns)
int_keys = ("Installation_Cost", "Annual_Energy_Savings", "Number_of_Devices")
float_keys = ("Customer_Satisfaction", "Latitude", "Longitude")
reconciled_v3 = [
    {"id": f"S{i:03d}", **{
        k: int(value) if k in int_keys else (float(value) if k in float_keys else value)
        for k, value in row.items()
    }}
    for i, row in enumerate(v3, 1)
]
assert len(v3) == 10
assert reconciled_v3 == canonical_smart, "V3 CSV != JSON: audit source drift"
assert embedded["smart_home"] == canonical_smart, "V3 inline HTML != JSON"
assert len({r["id"] for r in reconciled_v2}) == 49
assert len({r["id"] for r in reconciled_v3}) == 10
assert all(0 <= r["cost"] and 0 <= r["budgeted_cost"] for r in reconciled_v2)
assert all(-90 <= r["Latitude"] <= 90 and -180 <= r["Longitude"] <= 180 for r in reconciled_v3)
assert not re.search(r'<script\s+[^>]*src\s*=', HTML, re.I), "CDN would break offline mode"
assert "lang=\"pt-BR\"" in HTML
print("PASS: CSV(49+10), JSON, embedded HTML, unique IDs, totals and no remote JS")

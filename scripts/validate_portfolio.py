#!/usr/bin/env python3
"""Validate static Pages artifacts using Python standard library only."""
import json
import csv
from pathlib import Path
root = Path(__file__).resolve().parents[1]
site = root / 'site'
assert (site / 'index.html').exists(), 'Missing entry point'
html = (site / 'index.html').read_text('utf-8')
assert '<script>' in html and '<style>' in html
assert 'cdn.plot.ly' not in html and '<script src=' not in html
datasets = json.loads((site / 'api' / 'construction-v2.json').read_text('utf-8'))
smart = json.loads((site / 'api' / 'smart-home-v3.json').read_text('utf-8'))
assert len(datasets['records']) == 49
assert sum(x['cost'] for x in datasets['records']) == 3085000
assert sum(x['budgeted_cost'] for x in datasets['records']) == 2988000
assert len({x['id'] for x in datasets['records']}) == 49
assert len(smart['records']) == 10
# Cross-check the new CSV sources added to main (avoids silent data drift).
with (root / 'dashboards/v2_construction/data.csv').open(encoding='utf-8', newline='') as fh:
    csv_rows = list(csv.DictReader(fh))
assert len(csv_rows) == len(datasets['records'])
assert all(None not in row and None not in row.values() for row in csv_rows), 'Malformed CSV row / unescaped delimiter'
for row, original in zip(csv_rows, datasets['records']):
    assert row['pillar'] == original['pillar']
    assert row['service'] == original['service']
    assert int(row['cost']) == original['cost']
    assert int(row['budgeted_cost']) == original['budgeted_cost']
with (root / 'dashboards/v3_smart_home/data.csv').open(encoding='utf-8', newline='') as fh:
    smart_csv = list(csv.DictReader(fh))
assert len(smart_csv) == len(smart['records'])
for row, original in zip(smart_csv, smart['records']):
    assert row['City'] == original['city']
    assert int(row['Installation_Cost']) == original['installation_cost']

assert len({x['id'] for x in smart['records']}) == 10
for filename in ('dashboard_v1.html','dashboard_v2.html','dashboard_v3.html'):
    assert (site / filename).exists(), filename
print('PASS: HTML offline and example-data integrity')

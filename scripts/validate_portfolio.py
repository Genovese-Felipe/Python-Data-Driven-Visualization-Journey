#!/usr/bin/env python3
"""Validate static Pages artifacts using Python standard library only."""
import json
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
assert len({x['id'] for x in smart['records']}) == 10
for filename in ('dashboard_v1.html','dashboard_v2.html','dashboard_v3.html'):
    assert (site / filename).exists(), filename
print('PASS: HTML offline and example-data integrity')

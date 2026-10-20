#!/usr/bin/env python3
"""Validate embedded HTML datasets, JavaScript syntax, links and file structure."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("index.html", "dashboard_v1.html", "dashboard_v2.html", "dashboard_v3.html")
EXPECTED_COST = 3085000
EXPECTED_BUDGET = 2988000
errors = []
digests = set()

class Inspect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.duplicates = []
        self.scripts = []
        self.external = []
        self.relative = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if 'id' in d:
            if d['id'] in self.ids:
                self.duplicates.append(d['id'])
            self.ids.add(d['id'])
        if tag == 'script' and d.get('src'):
            self.external.append(d['src'])
        if tag == 'link' and d.get('href') and d.get('rel') == 'stylesheet':
            self.external.append(d['href'])
        if tag == 'a' and d.get('href') and not d['href'].startswith(('https:', 'http:', '#', 'mailto:')):
            self.relative.append(d['href'])

for name in NAMES:
    path = ROOT / name
    if not path.is_file():
        errors.append(name + ': absent')
        continue
    source = path.read_text(encoding='utf-8')
    dom = Inspect()
    dom.feed(source)
    if dom.duplicates:
        errors.append(name + ': duplicate IDs ' + str(dom.duplicates))
    if dom.external:
        errors.append(name + ': external scripts/stylesheets ' + str(dom.external))
    for href in dom.relative:
        if not (path.parent / href).exists():
            errors.append(name + ': invalid relative link ' + href)
    for marker in ('v1', 'v2', 'v3', 'sun', 'b2', 'scatter', 'pillar', 'region', 'tb2', 'tb3'):
        if marker not in dom.ids:
            errors.append(name + ': missing ID ' + marker)
    scripts = re.findall(r'<script(?:\s[^>]*)?>([\s\S]*?)</script>', source)
    if len(scripts) != 1:
        errors.append(name + ': expected single embedded script')
        continue
    js = scripts[0]
    match = re.search(r'const V2=(\[[\s\S]*?\]),V3=(\[[\s\S]*?\]);let tab=', js)
    if not match:
        errors.append(name + ': missing embedded JSON')
        continue
    try:
        v2, v3 = map(json.loads, match.groups())
    except json.JSONDecodeError as ex:
        errors.append(name + ': invalid dataset JSON ' + str(ex))
        continue
    digest = hashlib.sha256((match.group(1)+match.group(2)).encode()).hexdigest()
    digests.add(digest)
    if len(v2) != 49 or sum(x['cost'] for x in v2) != EXPECTED_COST or sum(x['budgeted_cost'] for x in v2) != EXPECTED_BUDGET:
        errors.append(name + ': V2 49-record monetary baseline drift')
    if len(v3) != 10 or sum(x['Installation_Cost'] for x in v3) != 131500:
        errors.append(name + ': V3 10-record installation baseline drift')
    keys = ('pillar', 'area', 'service', 'task', 'sub_task')
    if any(not all(x.get(k) for k in keys) or x['cost'] < 0 or x['budgeted_cost'] < 0 for x in v2):
        errors.append(name + ': V2 required fields/values invalid')
    if len({tuple(x[k] for k in keys) for x in v2}) != len(v2):
        errors.append(name + ': duplicated hierarchical V2 path')
    if shutil.which('node'):
        with tempfile.TemporaryDirectory() as tmp:
            f = Path(tmp) / 'inline.js'
            f.write_text(js, encoding='utf-8')
            result = subprocess.run(['node', '--check', str(f)], capture_output=True, text=True)
            if result.returncode:
                errors.append(name + ': JavaScript syntax invalid: ' + result.stderr[-500:])
    print(f'{name}: {len(source):,} chars; V2={len(v2)} V3={len(v3)}; dataset_SHA256={digest[:12]}')

if len(digests) != 1:
    errors.append('Standalone HTML pages disagree on embedded data.')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print('PASS: offline HTML structural, JSON arithmetic, parity and JS syntax checks.')
print('NOTE: browser, accessibility and visual regression tests remain outstanding.')

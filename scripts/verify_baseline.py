#!/usr/bin/env python3
"""Fail closed on historical data drift. Required before Pages deployment."""
from __future__ import annotations
import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def assigned_list(path: str, key: str):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
    for item in tree.body:
        if isinstance(item, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == key for t in item.targets
        ):
            return ast.literal_eval(item.value)
    raise AssertionError(f"Not found: {path}: {key}")


def main() -> None:
    source = assigned_list("dashboards/v2_construction/V2_script.py", "data")
    assert len(source) == 49, f"Expected 49 canonical V2 source rows, found {len(source)}"
    actual = sum(row["cost"] for row in source)
    budget = sum(row["budgeted_cost"] for row in source)
    assert (actual, budget) == (3085000, 2988000), (actual, budget)

    html = (ROOT / "index/dashboard_v2.html").read_text(encoding="utf-8")
    match = re.search(r"const\s+constructionData\s*=\s*\[([\s\S]*?)\]\s*;", html)
    assert match, "HTML V2 const constructionData not found"
    rows = re.findall(r"\{([^{}]*\bcost\s*:\s*\d+[^{}]*)\}", match.group(1))
    js_cost = sum(int(re.search(r"\bcost\s*:\s*(\d+)", r).group(1)) for r in rows)
    js_budget = sum(int(re.search(r"\bbudgeted_cost\s*:\s*(\d+)", r).group(1)) for r in rows)
    assert (js_cost, js_budget) == (actual, budget), (
        f"V2 parity FAIL: source cost/budget={actual}/{budget}, "
        f"HTML={js_cost}/{js_budget}; regenerate HTML from canonical data"
    )

    v1 = "dashboards/v1_simple/sunburst_cost_explorer_funcional.py"
    sizes = {x: len(assigned_list(v1, x)) for x in ("labels", "parents", "values")}
    assert len(set(sizes.values())) == 1, f"V1 hierarchy lengths incompatible: {sizes}"

    for name in ("dashboard_v1.html", "dashboard_v2.html", "dashboard_v3.html"):
        s = (ROOT / "index" / name).read_text(encoding="utf-8")
        assert "plotly-latest.min.js" not in s, f"Legacy Plotly CDN in {name}"

    print("PASS: source parity, V1 hierarchy cardinality, static runtime links")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"RELEASE BLOCKED: {exc}", file=sys.stderr)
        raise SystemExit(1)

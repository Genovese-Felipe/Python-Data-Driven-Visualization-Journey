#!/usr/bin/env python3
"""Smoke tests da auditoria 2026-10-20 (P02/P03/P06)."""
import importlib.util
import pathlib

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_v2_schema_and_totals():
    df = pd.read_csv(ROOT / "dashboards/v2_construction/data.csv")
    assert {"pillar", "area", "service", "cost", "budgeted_cost"} <= set(df.columns)
    assert (df["cost"] >= 0).all()
    assert int(df["cost"].sum()) == 3_085_000  # guarda P06
    assert int(df["budgeted_cost"].sum()) == 2_988_000
    assert df["pillar"].nunique() == 4


def test_v3_schema():
    df = pd.read_csv(ROOT / "dashboards/v3_smart_home/data.csv")
    assert {"Installation_Cost", "Annual_Energy_Savings", "Number_of_Devices",
            "Customer_Satisfaction", "Latitude", "Longitude"} <= set(df.columns)
    assert len(df) == 10  # toy dataset declarado


def test_apps_import():
    v1 = _load("v1", "dashboards/v1_simple/sunburst_cost_explorer_funcional.py")
    v3 = _load("v3", "dashboards/v3_smart_home/Plan_V3_funcional.py")
    assert v1.app is not None and v3.app is not None


def test_no_deprecated_cdn():
    for page in (ROOT / "index").glob("*.html"):
        text = page.read_text(encoding="utf-8")
        assert "plotly-latest" not in text, f"{page.name}: CDN descontinuado (P04)"
"""Smoke tests for the dashboard applications (V1-V4).

These tests verify that each dashboard module loads correctly, that the
data sources are present and well-formed, and that the predictive model
used by the V3 dashboard trains without errors. They must run from the
repository root (enforced by the repo_root_cwd fixture below).
"""
import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]

V1_PATH = REPO_ROOT / "dashboards" / "v1_simple" / "sunburst_cost_explorer_funcional.py"
V2_PATH = REPO_ROOT / "dashboards" / "v2_construction" / "V2_script.py"
V3_PATH = REPO_ROOT / "dashboards" / "v3_smart_home" / "Plan_V3_funcional.py"
V4_PATH = REPO_ROOT / "dashboards" / "v4_juridical" / "V4_juridical_dashboard.py"

V2_DATA = REPO_ROOT / "dashboards" / "v2_construction" / "data.csv"
V3_DATA = REPO_ROOT / "dashboards" / "v3_smart_home" / "data.csv"

V2_COLUMNS = {
    "pillar", "area", "service", "task", "sub_task", "cost", "budgeted_cost",
}
V3_COLUMNS = {
    "Region", "City", "Installation_Type", "Installation_Cost",
    "Annual_Energy_Savings", "Number_of_Devices",
    "Customer_Satisfaction", "Latitude", "Longitude",
}


@pytest.fixture(autouse=True)
def repo_root_cwd(monkeypatch):
    """Dashboard scripts read their CSVs relative to the repository root."""
    monkeypatch.chdir(REPO_ROOT)


def _import_app(path, extra_sys_path=None):
    """Import a standalone dashboard script as a module (no package needed)."""
    if extra_sys_path is not None and str(extra_sys_path) not in sys.path:
        sys.path.insert(0, str(extra_sys_path))
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[path.stem] = module
    spec.loader.exec_module(module)
    return module


def test_all_dashboard_files_exist():
    for path in (V1_PATH, V2_PATH, V3_PATH, V4_PATH):
        assert path.is_file(), f"missing dashboard file: {path}"
    for data in (V2_DATA, V3_DATA):
        assert data.is_file(), f"missing data file: {data}"


def test_v2_data_columns():
    import pandas as pd

    df = pd.read_csv(V2_DATA)
    assert V2_COLUMNS <= set(df.columns)
    assert len(df) > 0
    assert (df["cost"] >= 0).all()


def test_v3_data_columns():
    import pandas as pd

    df = pd.read_csv(V3_DATA)
    assert V3_COLUMNS <= set(df.columns)
    assert len(df) > 0


def test_v1_app_loads():
    module = _import_app(V1_PATH)
    assert module.app is not None
    assert module.app.layout is not None


def test_v2_app_loads():
    module = _import_app(V2_PATH)
    assert module.app is not None
    assert not module.df_budget.empty


def test_v3_app_loads():
    module = _import_app(V3_PATH, extra_sys_path=V3_PATH.parent)
    assert module.app is not None
    assert len(module.feature_importance) == 3


def test_v4_app_loads():
    module = _import_app(V4_PATH)
    assert module.app is not None


def test_v3_model_training():
    sys.path.insert(0, str(V3_PATH.parent))
    try:
        import model as v3_model  # noqa: E402  (dashboards/v3_smart_home/model.py)
    finally:
        sys.path.remove(str(V3_PATH.parent))

    import pandas as pd

    df = pd.DataFrame(
        {
            "Installation_Cost": [15000, 9000, 22000, 12000, 18000],
            "Number_of_Devices": [8, 5, 12, 6, 10],
            "Customer_Satisfaction": [4.2, 3.8, 4.6, 4.0, 4.3],
            "Annual_Energy_Savings": [1800, 950, 2600, 1200, 2100],
        }
    )
    fitted, importance = v3_model.train_energy_savings_model(df)
    assert len(fitted.coef_) == 3
    assert len(importance) == 3
    assert (importance["importance"] >= 0).all()

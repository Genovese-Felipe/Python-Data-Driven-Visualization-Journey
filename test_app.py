#!/usr/bin/env python3
"""Smoke checks do app raiz — corrigido na revisao 2026-10-20 (P03).

Antes: sys.path.append('/workspaces/Py_Vy_000') quebrava qualquer execucao
fora do codespace antigo e o script nao tinha asserts (nao era pytest).
"""
from sunburst_cost_explorer_app import app, create_enhanced_sunburst, df_budget, pillar_colors


def test_loads():
    assert app is not None
    assert len(df_budget) > 0
    assert {"cost", "budgeted_cost"} <= set(df_budget.columns)
    assert len(pillar_colors) >= 4


def test_sunburst_builder():
    fig = create_enhanced_sunburst(df_budget.head(10))
    assert fig is not None
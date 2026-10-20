#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V1 — Hierarchical cost explorer reconstructed from reconciled V2 leaf records.

This module intentionally replaces the legacy 97-label/53-value Sunburst lists.
Its source is the audited 49-row construction CSV, loaded relative to this file.
All amounts remain illustrative demonstration values; not actual observed costs.
The original historical implementation remains available in Git history.
"""
from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

DATA_FILE = Path(__file__).resolve().parents[1] / "v2_construction" / "data.csv"
df = pd.read_csv(DATA_FILE)
COLS = ["pillar", "area", "service", "task", "sub_task", "cost", "budgeted_cost"]
assert all(col in df.columns for col in COLS), "V1: missing CSV columns"
assert len(df) == 49, "V1: unexpected construction-record count"
assert not df[COLS].isna().any().any(), "V1: null hierarchy/cost value"
assert float(df["cost"].sum()) == 3085000, "V1: cost checksum mismatch"
assert float(df["budgeted_cost"].sum()) == 2988000, "V1: budget checksum mismatch"

app = Dash(__name__)
app.title = "V1 · Hierarchical Construction Explorer"
app.layout = html.Main(
    [
        html.H1("🏗️ V1 — Construction hierarchy"),
        html.P("Dados demonstrativos reconstruídos com IDs implícitos por caminho único."),
        html.Label("Pilar"),
        dcc.Dropdown(
            id="pillar",
            options=[{"label": "Todos os pilares", "value": "ALL"}]
            + [{"label": p, "value": p} for p in sorted(df.pillar.unique())],
            value="ALL",
            clearable=False,
        ),
        html.Div(id="summary", style={"padding": "14px 0"}),
        dcc.Graph(id="sunburst"),
        html.P(
            "Os custos são exemplos pedagógicos presentes nos scripts históricos; "
            "não representam execução financeira auditada."
        ),
    ],
    style={"fontFamily": "system-ui", "maxWidth": "1160px", "margin": "auto", "padding": "22px"},
)


@app.callback(Output("sunburst", "figure"), Output("summary", "children"), Input("pillar", "value"))
def update_dashboard(pillar):
    subset = df if pillar in (None, "ALL") else df.loc[df["pillar"] == pillar]
    costs = int(subset["cost"].sum())
    budget = int(subset["budgeted_cost"].sum())
    fig = px.sunburst(
        subset,
        path=["pillar", "area", "service", "task", "sub_task"],
        values="cost",
        color="pillar",
        title="Construction cost decomposition",
    )
    fig.update_traces(
        hovertemplate="<b>%{label}</b><br>Cost: $%{value:,.0f}<br>"
        "Parent share: %{percentParent:.1%}<extra></extra>"
    )
    fig.update_layout(
        height=670, margin=dict(t=80, l=12, r=12, b=12), font=dict(size=12)
    )
    summary = html.Div(
        [
            html.Strong(f"Cost: ${costs:,.0f}"),
            html.Span(f"  ·  Budget: ${budget:,.0f}"),
            html.Span(f"  ·  Delta: ${costs-budget:,.0f}"),
            html.Span(f"  ·  Records: {len(subset)}"),
        ]
    )
    return fig, summary


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=8052)

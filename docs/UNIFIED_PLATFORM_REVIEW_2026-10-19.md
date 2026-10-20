# FGen Data Intelligence — Unified Platform Review

**Status:** implementation proposal (not yet imported from ChatGPT artifact).
**Branch:** `review/unified-data-intelligence-2026-10-19` based on the *current* `main`.
**Review gate:** leave `main` and existing PR #9 unchanged; do not merge automatically.

## Confirmed baseline and conflict

- Primary `main`: 62 tracked files; PR #9 review branch: 61 files; PR audit documents 53 files from an older base.
- The PR #9 branch diverged from `main` (7 commits on current main vs 10 on PR branch).
- Newly added `dashboards/v2_construction/data.csv` has 49 cost records (USD 3,085,000 cost, 2,988,000 budget). Some `task` fields contain unquoted commas and require CSV normalization before parsing.
- `dashboards/v3_smart_home/data.csv` has 10 illustrative records; it does NOT prove a predictive model.
- `dashboards/v4_juridical/V4_juridical_dashboard.py` does not yet exist on current main.
- Predictive Analytics companion: `docs/index.html` advertises an unrelated audio remix collection; `dashboard_app/app.py` binds `project-table.data` to an `html.Div`, while the callback returns an HTML table. Correct to `children` or use `dash_table.DataTable`.
- Companion static exporter loads Plotly through CDN, so its output is NOT strictly offline.
- Handbook: code license MIT; separate text license CC BY-NC-ND 3.0. Link or cite source; do not copy textbook wholesale.

## Target design

1. Keep old Python dashboards as legacy examples; normalize V2 and V3 datasets, with independent validated contracts.
2. Build a standalone HTML/JS/SVG site with tabs V1 (reconstructed from V2), V2, V3 and new fictitious V4; embed all required resources.
3. Preserve synthetic/disclaimer flags. No legal personal data in public GitHub Pages.
4. Supply `data/canonical_bundle.json`, `site/manifest.json`, `AGENTS.md`, and reproducible build/check commands.
5. Run deterministic CI and optional browser tests; require owner approval before Pages publication.
6. Adopt the companion repo's `dashboard_app/` architecture for server-side Python but keep GitHub Pages static-only.

## Proposed imported artifact layout

```
site/index.html
site/dashboard_v{1,2,3,4}.html
tools/build_portfolio.py
tools/validate_portfolio.py
tools/template.html
data/v2_construction.csv
data/v3_smart_home.csv
data/v4_juridical_synthetic.json
data/canonical_bundle.json
dashboards/v4_juridical/V4_juridical_dashboard.py
tests/test_portfolio.py
.github/workflows/ci.yml
.github/workflows/pages.yml
AGENTS.md
docs/AUDIT_REPORT.md
```

The built bundle has been generated separately for review in ChatGPT, **not committed to this branch**. Import only after reviewing data provenance, scripts, tests and asset licensing.

## Acceptance gates

- `python tools/build_portfolio.py` and `python tools/validate_portfolio.py` succeed.
- All five pages work without CDN or runtime server-side code, with no console errors.
- V2 totals unchanged, V3 flagged synthetic, V4 contains DEMO-* records only.
- CSV export, filters, mobile layout, keyboard accessibility and file:// behavior verified.
- No Pages deployment from unreviewed pull requests or branches.

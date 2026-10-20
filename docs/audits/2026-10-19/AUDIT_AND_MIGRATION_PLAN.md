# Audit and migration plan — 2026-10-19

> REVIEW BRANCH ONLY. Base `main` SHA: `859aa2882b290268d46d7027b4eb437cb844914b`. Do not merge until acceptance gates below pass.
> Method: GitHub tree and source inspection, programmatic cross-source comparisons. No claim of running the historical Dash apps end-to-end.

## Confirmed source findings
| ID | Severity | Source | Evidence | Action |
|---|---|---|---|---|
| P01 | Critical | `dashboards/v1_simple/sunburst_cost_explorer_funcional.py` | 97 labels, 97 parents, 53 values, 45 colors; invalid cardinality for hierarchical metrics | Normalize hierarchical leaf data and explicitly aggregate parent nodes |
| P02 | High | `dashboards/v2_construction/V2_script.py` vs `index/dashboard_v2.html` | Python 49 rows: costs 3,085,000, budget 2,988,000; HTML 23 summary rows: costs 4,730,000, budget 4,557,000 | Canonical JSON/CSV, generated website, parity tests |
| P03 | High | V2 HTML vs Python | `Construction` Python 2,025,000 vs HTML 3,370,000; Python `Management` 405,000 vs HTML 435,000 | Disallow handwritten parallel datasets |
| P04 | High | `dashboards/v3_smart_home/Plan_V3_funcional.py` | 10 coded example rows; `model.fit(X,y)` on all 10; no CV/evaluation in script | Identify synthetic source; baseline, LOOCV, leakage review, holdout when more data exist |
| P05 | High | `index/dashboard_v1.html`, V2, V3 | `plotly-latest.min.js` is legacy frozen release, external runtime dependency | Pin current version or embed Plotly JS in released artifacts |
| P06 | High | Page entry | `index/principal.html` exists, but no site-root `index.html`; Pages branch source only supports root or `/docs` | Actions deployment of built `_site/index.html` |
| P07 | High | `main` GitHub API | Branch `protected:false` | Enable branch protection / ruleset (admin setting) |
| P08 | Medium | `run_app.py`, `app_simples.py`, `test_dash_simple.py` | Legacy `app.run_server` with debug and all-interface binding | Modernized Dash entry points, env-based safe debug settings |
| P09 | High | `test_app.py` | Fixed `sys.path.append('/workspaces/Py_Vy_000')`; print-only smoke check | Pytest test functions, repo-relative imports, CI |
| P10 | High | `dashboards/v3_smart_home/Plan_V3.py` | `df_complex` referenced before defined/imported, numeric predictors one-hot encoded as categories | Explicit dataset import, direct numeric features, validated modelling |
| P11 | Medium | `dashboards/v2_construction/V2_script.py` | Plotly hover template expression `%{(customdata[0] - customdata[1])}` not a supported computed field | Calculate variance column before plotting |
| P12 | High | `index/dashboard_v3.html` | Model-importance plot uses `[0.75,0.85,0.15]` labelled simulated; not Python model coefficients | Use validated model export, or badge as illustrative |
| P13 | Medium | `docs/API_REFERENCE.md` | Documents aspirational functions e.g. `train_energy_model` not defined in inspected app modules | Generate API reference from actual package |
| P14 | Medium | Notebook files | 3 notebooks; embedded error outputs: 1, 2, 3 respectively | Isolated notebook execution, remove stale error states only after fixing |
| P15 | Medium | `docs/plotly_python_guide.xml` | 2.8MB blob; content unavailable from text fetch due tool size, metadata only | Download locally and XML schema/parse test before sign-off |
| P16 | Medium | `Plotly_Guides/About_Guides_XLMextratction.md` | 1 byte, effectively empty | Populate purpose or remove via approved migration |
| P17 | Medium | `Plan_Data_V3.py` and folder copy | Same SHA; unseeded synthetic random data; differs from V3 embedded fixed dataset | Single reproducible generator with explicit seed |
| P18 | Low | `index/principal.html` | Navigation `href="#"` for Home | Replace with working `index.html` link |
| P19 | Medium | `requirements.txt` | 2023–24 pins, no lock strategy or security audit workflow | Rebase tested dependency constraints; uv/pip-tools; pip-audit |
| P20 | Medium | `README.md`/`RELEASE_NOTES.md` | Claims 3/3 complete and real data, inconsistent with sample data and static findings | Badge actual CI status, provenance and demo disclaimer |

## Data reconciliation (confirmed)
- V2 Python: **49 source rows** aggregated into **23 service groups**; 3,085,000 actual, 2,988,000 budget, 97,000 delta (3.246% of budget).
- By Python pillar: Project Design 315,000; Management 405,000; Construction 2,025,000; Finishing & Landscaping 340,000.
- HTML V2: 23 hardcoded summary rows, 4,730,000 actual, 4,557,000 budget. Not equivalent despite similar labels.
- V3 Python and V3 HTML each embed 10 demonstrative observations; they must be described as **illustrative**, not real installed-device readings.

## Proposed structure (additive first)
```
data/
  raw/                  # retained original inputs where licensing permits
  curated/
    construction_v2.csv # exactly 49 rows, validated
    smart_home_demo.csv # exactly 10 rows, DEMO label
src/visualization_journey/
  datasets.py
  charts.py
  models.py
  app.py
scripts/
  validate_data.py
  export_static.py
site/
  index.html
  v1.html
  v2.html
  v3.html
tests/
  test_data_parity.py
  test_hierarchy.py
  test_dash_callbacks.py
  test_ml_baseline.py
  test_pages_links.py
.github/workflows/
  ci.yml
  pages.yml
```

## GitHub Pages: recommended release mechanism
GitHub Pages cannot execute server-side Dash/Python. Export to static HTML (Plotly `to_html(full_html=True,include_plotlyjs=True)`, or a dependency-free SVG+JS adaptation). For Actions, assemble `site/` as artifact root and run `actions/configure-pages`, `actions/upload-pages-artifact`, `actions/deploy-pages` with pages:write/id-token:write. Configure **Settings → Pages → Source: GitHub Actions**. Do not deploy this review branch over production without explicit approval.

### Alternative minimal build with existing pages
```bash
mkdir -p _site
cp index/principal.html _site/index.html
cp index/dashboard_v{1,2,3}.html _site/
touch _site/.nojekyll
```
This only fixes the site's entry point; **it does not fix the monetary inconsistency or CDN dependency**. It must not pass the production content gate as-is.

## Phased implementation, PR-sized
1. **W0 — Baseline**: tag baseline SHA, inventory all files and document source data/licensing. No deletions.
2. **W1 — Correctness P01–P04**: unify dataset; ensure totals, hierarchy, filtered subtotals, and model claims are tested. CI required.
3. **W2 — Static export P05–P06/P12**: build fully offline releases and site bundle from one source; responsive/a11y smoke.
4. **W3 — Quality P08–P11/P13–P19**: factor package, test callbacks, notebook execution, pinned deps and audit.
5. **W4 — Documentation**: screenshot previews, accessibility text, README PT/EN, CHANGELOG and links.
6. **W5 — Deployment**: manually enable Pages Actions, stage and verify preview. Merge only by approved PR, protected main.

## Acceptance gates
- [ ] Canonical data totals: cost 3,085,000; budget 2,988,000; delta 97,000.
- [ ] All V1 hierarchy nodes: unique ID, valid parent, correct aggregate value.
- [ ] V2 Python, generated JSON, Dash and HTML totals identical under filters.
- [ ] No hidden `plotly-latest`, unpinned CDN or runtime external dependency in offline release.
- [ ] V3 synthetic provenance explicit; ML metrics out-of-sample or claim removed.
- [ ] Python syntax, Ruff, pytest, pip-audit; client JS syntax and Playwright interaction checks.
- [ ] 320px mobile layout, keyboard navigation, SVG labels, alt text, page entry and links.
- [ ] Pages preview approved; no write to `main` except reviewed merge.

## Risk note
Branch creation and this report do **not** configure the Pages repository setting, enable branch protection or deploy a site. Those are controlled release operations. All claims about historical runtime behavior are provisional until CI execution.

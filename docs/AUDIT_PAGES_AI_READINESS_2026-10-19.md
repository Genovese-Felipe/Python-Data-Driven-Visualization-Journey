# Audit + public portfolio implementation plan

Baseline `859aa2882b290268d46d7027b4eb437cb844914b` · Audit branch `audit/pages-ai-readiness-20261019` · Date 2026-10-19.

## Evidence classes
- **Verified**: source inspected or deterministic computed consistency check.
- **Risk**: failure plausible by source reading, requires execution to confirm.
- **Not tested**: external reachability, performance, browser support and live ML quality.

## P0 / P1 defects
| ID | Evidence | Recommended fix | Acceptance test |
|---|---|---|---|
| A01 | V1 labels=97, parents=97, values=53 in Python | Replace parallel arrays with normalized tree; build valid parent IDs and aggregation invariant | all sunburst nodes resolve parents and sums |
| A02 | V2 Python 49 line items 3,085,000/2,988,000 vs original HTML 23 records 4,730,000/4,557,000 | Canonical dataset generator, explicit provenance and one render pipeline | browser and Python KPI equality |
| A03 | V3 trains on 10 sample rows, no held-out metrics | Baseline, LOOCV, MAE/RMSE, confidence and residual checks; no predictive claims | external sample performance report |
| A04 | `plotly-latest.min.js` legacy unversioned CDN | Offline native SVG/JS (review implementation) or pin and vendor Plotly | 0 network requests to render |
| A05 | Existing `index/principal.html`, not a source-root `index.html` | Build deployable `site/index.html` + GitHub Actions upload | site root returns HTML 200 after deployment |
| A06 | `main` protection disabled on inspection | Enforce PR review, required test checks and no direct push | branch protection/ruleset active |
| A07 | `run_app.py`, `app_simples.py`, `test_dash_simple.py` call legacy Dash `run_server()` | Version-aware entrypoint, update documentation and dependency lock | Python smoke test current Dash |
| A08 | `test_app.py` hard-coded `/workspaces/Py_Vy_000` | use package-relative path and pytest fixtures | tests run in clean Github Actions runner |
| A09 | Notebooks contain cached error outputs | isolate requirements / restart-run-all + export sanitized notebooks | 0 unresolved error outputs and reproducible kernels |
| A10 | README/release notes refer to example data as “real” | change to illustrative/reconstructed and provide provenance | all data claims carry source/limitations |
| A11 | API_REFERENCE describes functions not confirmed in source inventory | generate API docs from AST / public interfaces | documented symbols import and run |
| A12 | V1/ V2 duplicated hierarchy labels with inconsistent naming | stable IDs / canonical codebook and cross-view consistency tests | deterministic mapping with no orphan category |

## Delivery stages and explicit checkpoints
1. **Baseline + gate (P0):** freeze SHAs, save manifest, set up PR + CI; never commit directly to main.
2. **Data contracts (P0):** normalize 49 cost rows and 10 smart-home rows; add schemas, ids, units, provenance, static JSON.
3. **Web (P1):** static responsive browser app; offline; keyboard-accessible charts, filters, explicit demo-data notice; CSV export.
4. **Python (P1):** repair legacy Dash and notebooks in separate commits; test them independently of static Pages.
5. **Model quality (P1):** evaluate V3 baseline / LOOCV, remove unvalidated “predictive” overclaim.
6. **Docs (P1):** bilingual README with verified examples, architecture diagram, Pages links after first deployment.
7. **External agents (P2):** machine-readable catalog and JSON, GitHub raw asset URLs, documented local/cloud execution commands; never expose API keys in browser.
8. **Deploy (release gate):** enable Settings → Pages → Source GitHub Actions, merge verified PR, confirm Pages URL/smoke tests then publish announcement.

## Hosting distinctions
- GitHub Pages runs HTML/CSS/JS and distributes JSON. It **does not run server-side Python/Dash or arbitrary external AI jobs**.
- For Python runtime choose GitHub Actions scheduled/manual batch build, Colab, Codespaces, Hugging Face Spaces Docker, or a hosted app.
- For LLM/API integration use a securely deployed backend with secrets, auth, rate limits and CORS; Pages consumes backend through a public API only when enabled.
- Static catalog is publicly machine-readable once Pages deployment is enabled; agents can also read GitHub repository files via authenticated GitHub API.
- No automated deploy from the audit branch; workflow deploys only after changes land on `main`.

## Risks / rollback
- Pages currently could be configured for another source: inspect Settings before switching.
- Unvalidated examples must not become engineering quotations or professional advice.
- User privacy: strip outputs from notebooks and image metadata before publishing externally.
- Rollback: revert merge commit or re-deploy previously known artifact. Preserve original `main` commit.

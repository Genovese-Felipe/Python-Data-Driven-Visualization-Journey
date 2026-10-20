# Implementation Plan — audit/pages-v4-review-20261019

## Status
Draft PR #12. No edits to main from this review. The active main diverged by 7 commits during review, including its own Pages workflow and newer Smart Home model.py/data.csv. Rebase, reconcile the workflow and regenerate the Smart Home dataset before any merge.

## Architecture
- pages/index.html: gallery and machine-readable catalog entry point.
- pages/v1.html: interactive reconstructed V1 using valid V2 synthetic data, not the 53 broken original values.
- pages/v2.html: 49 V2 leaves, 3,085,000 cost and 2,988,000 budget in unspecified monetary units; interactive filters, sunburst, treemap, bars and table.
- pages/v3.html: 10 synthetic installation samples, filters, scatter chart, coordinate map without external tiles and regional aggregates; no validated ML claims.
- pages/assets/app.js and style.css: static interactive frontend.
- pages/catalog.json, construction_costs.csv, smart_home.csv: machine-readable interfaces for AI tools.
- scripts/verify_pages.py: source counts, financial reconciliations and basic HTML tests.
- .github/workflows/pages.yml: build on PR; deployment only on approved main pushes.

## Gates — before merge or live deploy
1. Rebase this branch onto current main; resolve pages.yml add/add conflict and keep exactly one Pages deployment workflow.
2. Update Smart Home source handling to the newly introduced CSV/module layout; confirm data provenance.
3. Run Python verifier, JS syntax, browser E2E mobile/desktop, keyboard/contrast checks and empty-data tests.
4. Confirm the Github Pages workflow generates assets/plotly.min.js; pages files alone do not include that bundle.
5. In repository Settings > Pages, choose GitHub Actions as publishing source.
6. Only after reviews/checks and merge should push main publish the static site.

## External AI execution
Static clients read catalog.json and the CSVs. Python-capable agents clone the repo and invoke scripts/verify_pages.py. Dash apps cannot run on GitHub Pages; a backend/container/Colab is necessary for callbacks, Python tasks or model inference. Do not expose private Apartment 91 cost data without authorization.

## Known limits
Full file inventory and focused critical-code inspection completed; visual review of binary images, comprehensive XML semantic review, full notebook reexecution and browser end-to-end checks remain open. No public Pages URL has been verified live.
## Additional regression in newly changed main V3
The current main V3 script imports `from .model import train_energy_savings_model` but the legacy README instructs users to run that file directly as `python dashboards/v3_smart_home/Plan_V3_funcional.py`. Direct execution lacks a package context and normally raises `ImportError: attempted relative import with no known parent package`. The relative `pd.read_csv('dashboards/v3_smart_home/data.csv')` also depends on the caller's working directory. Proposed fix: choose module entry point (`python -m dashboards.v3_smart_home.Plan_V3_funcional` plus packages where required), or absolute package imports; use `Path(__file__).resolve().parent / 'data.csv'`; add CI smoke tests for both invocation paths before adopting the newly changed V3.

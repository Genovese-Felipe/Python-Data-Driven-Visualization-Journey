# AGENTS.md — execution contract for outside AI agents

Read pages/catalog.json before interpreting demo assets. All datasets are synthetic, read-only and denominated in unspecified monetary units; these are not Apartment 91 actual construction costs.

To inspect without execution: load pages/construction_costs.csv (49 leaves), pages/smart_home.csv (10 records), and the versioned catalog. To check consistency: python scripts/verify_pages.py. To preview a built Pages artifact: serve the _site folder with python -m http.server; it must include assets/plotly.min.js.

Construction schema: pillar, area, service, task, sub_task, cost, budgeted_cost. Treat each row as a leaf. Unique node IDs are a serialization of the complete path, not the label. Require all parents to exist and each parent total to equal the sum of child totals for both additive cost and budget. Signed variance cannot define geometric area.

V1 website demo reuses V2 data to repair the invalid legacy V1 parent graph; do not represent it as the authentic V1 dataset. V3 ten-sample regression coefficients are not validated predictive feature importance. Do not claim ML accuracy.

GitHub Pages is static: HTML/JS can filter, chart and export in the browser, but cannot run a Python Dash server, train a model, or expose arbitrary authenticated Python execution. Use a separate trusted compute environment and explicit API if dynamic execution is required.

Repository updates: use feature branches, tests and draft PR; do not push directly to main or auto-merge. An unrelated series of main changes appeared during this audit; reconcile before integrating. Protect personal or commercial documents before any public publication.
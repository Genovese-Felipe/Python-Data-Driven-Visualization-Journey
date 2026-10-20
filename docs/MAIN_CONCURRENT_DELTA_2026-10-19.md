# Audit delta after concurrent main updates (2026-10-19)

- Historical audited main: `859aa288...`, **53 blobs**.
- First concurrent main snapshot: `beff5d65...`, **56 blobs**, added Pages workflow, visual README proposal and earlier audit.
- Latest re-examined main: `20486531a623c48e99bf6e529e13c28155b56603`, **62 blobs**, +6 CSV/model files, modified 10 source files.
- This review branch is merged **from** current main but is not merged **into** main.

## Corrections already materialized in main
1. V2 example data moved to `dashboards/v2_construction/data.csv` (49 cost lines, amount sums consistent with the original V2 Python).
2. V3 example data moved to `dashboards/v3_smart_home/data.csv` (10 sample installations).
3. V3 model extracted to `dashboards/v3_smart_home/model.py`; however evaluation still fits on the 10 sample lines, so it is not externally validated.
4. Other root apps now consume extracted CSV fixtures in `data/`, reducing duplication.
5. Workflow for legacy static Pages deployment was added and GitHub Actions reported a successful main deployment.

## New regression found in main
`Plan_V3_funcional.py` now imports `from .model import train_energy_savings_model`. The README's documented direct command `python dashboards/v3_smart_home/Plan_V3_funcional.py` lacks a parent package context and cannot resolve the relative import. The review branch fixes this with a `__package__`-aware import.

## Unresolved
- V1 still has vectors of **97 labels, 97 parents, 53 values**, not a valid aligned Sunburst data contract.
- Legacy HTML V2 remains different from the Python/CSV V2 dataset.
- The V2 Dash hovertemplate contains an unsupported arithmetic expression in a Plotly variable placeholder; needs explicit precomputed customdata.
- Runtime Dash, complete notebook clean-run, XML semantic audit, asset rights, WCAG/mobile and published-site HTTP smoke still require independent verification.
- External AI CLI is implemented with data/JSON tests; GitHub Pages still cannot execute Python server-side.

## Review strategy
- Preserve current main's Python/CSV refactors.
- Override only reviewed `.github/workflows/pages.yml`, README, site/, docs, validators and agent interface, with explicit audit rationale.
- Publish new offline dashboard under /, existing legacy HTML under /legacy/.
- Gate any merge on checks and owner review.

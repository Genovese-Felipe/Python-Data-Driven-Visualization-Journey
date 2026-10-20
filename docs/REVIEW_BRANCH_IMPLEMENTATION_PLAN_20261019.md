# Review branch: audit + self-contained dashboards (2026-10-19)

**Branch:** `review/audit-pages-selfcontained-20261019`  
**Base:** main at branch creation.  
**Safety:** no modifications to main are permitted without PR review/explicit merge.

## Goal
Repair source-level Sunburst inconsistencies, make the public HTML dashboards V1/V2/V3 fully offline, and formalize a reproducible static GitHub Pages build. The Apartment 91 records are **private by default** and not part of the public site.

## Audit evidence
- Original snapshot: 53 paths; latest reviewed tree: 56 paths after three concurrently added files appeared on main (.github/workflows/pages.yml, README_VISUAL_PROPOSTA.md, docs/AUDITORIA_PAGES_2026-10-19.md).
- V1: 97 labels, 97 parents, 53 numeric values; parallel vectors must be replaced with a normalized leaf table.
- Plotly Sunburst using branchvalues=total requires parent totals to equal the sum of child totals.
- Current index/dashboard_v1.html, v2.html, and v3.html use an unversioned plotly-latest CDN.
- run_app.py, app_simples.py, test_dash_simple.py still use app.run_server; V2 and one V3 entry use Jupyter inline launch.
- V3 model has only ten simulated samples; coefficient absolute magnitudes should not be reported as scientifically validated feature importance.
- Current .github/workflows/pages.yml copies existing HTML rather than generating versioned offline pages. Coordinate a single workflow in PR review.

## Implementation plan and review gates
1. Preserve all historic Python/Notebook code; no wholesale replacement.
2. Introduce synthetic JSON datasets, schemas and AGENTS.md execution contract.
3. Add deterministic Python builder producing site/index.html and three independent offline HTML dashboards with embedded Plotly.js.
4. Ensure all Sunburst ancestor IDs are unique, cost totals are conserved, KPI filters are synchronized, and no phantom WBS or actual costs are created.
5. Add automated CI tests for datasets, frontend presence, offline bundles and absence of private AP91 records.
6. Replace the existing Pages workflow only after comparing with the concurrently added workflow. PR should build and test but must **not deploy**.
7. README gallery is bilingual, readable and grounded: demos synthetic, AP91 audit local-only.
8. Manually test browser interactions (Chromium desktop/mobile), keyboard use, performance, and any external file publishing gates.
9. Merge only after approval. Deployment to GitHub Pages is a post-merge step on main.

## Files prepared separately for review
A complete downloadable implementation package was prepared during the ChatGPT audit: `scripts/build_site.py`, `data/synthetic_*.json`, `data/schema_*.json`, `tests/test_publication.py`, `requirements-pages.txt`, `AGENTS.md`, `README_VISUAL_REVIEW.md`, `docs/AUDITORIA_E_PLANO.md`, `docs/auditoria_arquivo_a_arquivo.csv`, `site/*.html` and a local-only `private_ap91/` bundle.

**Important:** The package contents have not all been pushed to this branch. This Markdown document records the safe implementation and integration sequence. Never upload `private_ap91/` to GitHub.

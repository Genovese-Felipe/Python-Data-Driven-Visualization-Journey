# AGENTS.md — read-only external agent contract

## What this repository provides
- Offline browser dashboard artifacts: `site/index.html`, `site/dashboard_v1.html`, `site/dashboard_v2.html`, `site/dashboard_v3.html`.
- Versioned static JSON datasets: `site/api/catalog.json`, `site/api/construction-v2.json`, `site/api/smart-home-v3.json`.
- Deterministic Python CLI: `python scripts/agent_cli.py summary --dataset construction-v2`; `python scripts/agent_cli.py summary --dataset smart-home-v3`.
- Query example: `python scripts/agent_cli.py filter --dataset construction-v2 --field pillar --equals Construction`.
- GitHub Actions manual job: `.github/workflows/agents.yml` dispatches a read-only summary, uploads JSON artifact (requires repository permission/API access).

## Rules for external agents
1. **Do not write to `main`**, merge PRs, publish Pages or modify API contracts without explicit owner approval.
2. Treat all numerical datasets as **illustrative examples**, never as engineering budgets, real measured energy savings or verified prediction performance.
3. Respect provenance and `data_status`. Keep `dataset` identifier and revision SHA in any derived report.
4. Do not execute arbitrary user-provided source, shell commands or remote notebooks. CLI supports allowlisted commands and fields only.
5. No API keys, auth secrets or personal data in HTML, JS, JSON, logs, notebooks or GitHub Pages.
6. For real inference, run a separately authenticated backend (not GitHub Pages), with rate limits, input validation, logs and deployment controls.
7. Run `python scripts/validate_portfolio.py` and `python -m unittest discover -s tests -p 'test_agent_cli.py'` before proposing an update.

## Retrieval / execution patterns
- Browser via GitHub Pages after deployment; until then inspect branch blobs.
- Fetch raw `site/api/catalog.json` or datasets with GitHub HTTP API.
- External platform (Codespaces, Colab, Docker, Hugging Face Space) clones repository and runs the CLI or Dash Python apps with their own dependencies.
- GitHub Actions jobs are ephemeral batch runs, not live hosting. Pages serves static HTTP only.
- If actual Python Dash application is desired, deploy separately and serve a secure API or application link.

## Source-of-truth caveat
Historical HTML V2 differs from Python V2 and requires versioned names, not silent overwrite. The review static dataset is extracted from Python V2 (49 line items, USD 3,085,000 cost / 2,988,000 budget). Model V3 uses 10 illustrative rows and is not externally validated.

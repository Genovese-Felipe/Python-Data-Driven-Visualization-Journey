# VizLab — Machine operation contract

## Static discovery
A read-only agent fetches the deployed `catalog.json` and `api/{v1,v2,v3,v4}.json`. All data is public and illustrative. Dataset versions are independent.

## Local execution
```bash
python -m pip install -r vizlab/requirements.txt
python vizlab/build.py catalog
python vizlab/build.py validate
python vizlab/build.py build
```

## Workflow dispatch (after merge)
An AI agent **with user-authorized GitHub Actions permissions** can POST to:
`https://api.github.com/repos/Genovese-Felipe/Python-Data-Driven-Visualization-Journey/actions/workflows/vizlab-agent.yml/dispatches`

Payload: `{"ref":"main","inputs":{"operation":"validate"}}`.

The workflow must exist on the default branch; it does **not** run arbitrary code, only approved operations. The job artifact contains structured JSON and optional HTML.

## Limitations
GitHub Pages is static. It cannot run Python, Python Dash callbacks, arbitrary AI-generated code or protected ML inference. For live operations build a separately authenticated backend with explicit OpenAPI and rate limits. Never publish secrets. Never use untrusted pickle models. Review the license of external materials before copying.

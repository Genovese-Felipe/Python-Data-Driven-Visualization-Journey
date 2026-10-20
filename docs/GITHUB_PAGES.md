# GitHub Pages — receita de publicacao

## Estado atual

O repo ja tem .github/workflows/pages.yml correto (Actions-based): valida os 4 HTML de index/, monta _site (principal.html vira index.html, .nojekyll) e publica via actions/deploy-pages@v4. Nao usar 'Deploy from branch' — manter 'GitHub Actions' em Settings > Pages.

URL: https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/

## Passos

1. Settings > Pages > Source: GitHub Actions.
2. Merge da branch de revisao: ci.yml (testes + guards) e pages.yml (deploy) passam a rodar juntos.
3. Fix do CDN (P04): trocar https://cdn.plot.ly/plotly-latest.min.js por https://cdn.plot.ly/plotly-2.35.2.min.js nos 4 HTML.
4. Adicionar index/audit_hub.html ao loop de validacao e ao _site no pages.yml (ja proposto na branch).
5. Adicionar 404.html, robots.txt e favicon ao _site (Fase 3).

## Guards no CI (aplicados nesta branch)

- testes pytest 3.11/3.12 (P01/P02/P03).
- grep negativo por plotly-latest (P04).
- checagem de soma dos dados embutidos (P06) em tests/test_smoke.py.

## Nao fazer

- Nao servir docs/*.xml (4,2 MB) no Pages.
- Nao publicar notebooks com outputs.
- Nao depender de 'latest' em CDN.
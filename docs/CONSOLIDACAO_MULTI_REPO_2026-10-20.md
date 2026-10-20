# Consolidacao multi-repo — 2026-10-20

## Inventario cross-repo

| Repo | Natureza | Estado | Papel no hub |
|---|---|---|---|
| Python-Data-Driven-Visualization-Journey | jornada V1-V3 Plotly/Dash, site estatico Pages | auditado aqui (P01-P26) | dashboards 'journey' + portfolio estatico |
| Python-Data-Plotly-Predictive-Analytics-Dashboard | dashboard_app v2 (240 projetos sinteticos, holdout, export HTML, CI 3.10/3.12) | auditado 2026-10-19 (main @ 53a1db0, PR #41); callback Output('project-table','data') quebrado; site/docs vendem a v1 (25 projetos, R$ 15,2M, 'real-time') | dashboards 'construction analytics' 240 projetos |
| PythonDataScienceHandbook | fork do handbook (texto CC-BY-NC-ND, codigo MIT) | fork de referencia | somente consulta; nao copiar texto |

## Achados comuns (padrao cross-repo)

- Overclaim de dados ('reais', 'real-time') onde o dataset e sintetico.
- Duplicacao v1/v2 de produtos com docs vendendo a versao antiga.
- KPIs/metricas hardcoded divergentes dos dados.
- Falta de guard de CI sobre frontend/HTML.

## Proposta: hub consolidado 'Genovese Visual Analytics'

Estrutura de projeto novo (repo unico ou pasta docs-hub no repo maior):

    visual-analytics-hub/
    |- index.html            # hub self-contained, zero build
    |- dashboards/
    |   |- journey-v1.html   # sunburst (dados inline)
    |   |- journey-v2.html   # filtros cascata (49 linhas inline)
    |   |- journey-v3.html   # scatter + OLS (10 linhas inline)
    |   |- construction-240.html  # export do dashboard_app (Plotly Predictive)
    |- audit/
    |   |- matrix.json       # matriz de auditoria machine-readable
    |   |- audit_hub.html    # dashboard de auditoria
    |- .github/workflows/    # ci (pytest+guards) + pages (deploy)
    |- README.md             # tabela verdade por repo

Regras do hub:

- Cada dashboard e self-contained (dados inline JSON, Plotly por CDN versionado ou zero-dependencia SVG).
- Todo dashboard carrega um bloco JSON-LD 'regen' com fonte do dado, data de geracao e comando que o regenera — AI-externa executa o comando e diffa.
- Dados sinteticos rotulados em cada cabecalho.
- Pages publica so o hub; CI bloqueia plotly-latest e KPI divergente.

## Roadmap de consolidacao

1. Fase 1-3 da auditoria Journey (branch atual) — estabilizar o repo-alvo.
2. Mergear correcoes do Plotly Predictive (P01 callback children; docs honestos) — ja documentadas na auditoria 2026-10-19.
3. Criar repo hub; importar os exports; publicar Pages.
4. Automatizar regeneracao via workflow (AI-executavel).
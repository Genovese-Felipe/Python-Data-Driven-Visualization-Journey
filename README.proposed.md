# Python Data Driven Visualization Journey

<div align='center'>

**Visual analytics · Plotly/Dash · Data storytelling · Aprendizado por construcao**

![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB?logo=python&logoColor=white) ![Dash](https://img.shields.io/badge/Dash-2.16-0080A8?logo=plotly&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-5.17-3F4A75?logo=plotly&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-yellow) ![Dataset](https://img.shields.io/badge/Dados-sint%C3%A9ticos%20rotulados-orange)

[Dashboards no GitHub Pages](https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/) · [Auditoria integral 2026-10-20](docs/audit/AUDITORIA_INTEGRAL_2026-10-20.md) · [Como publicar no Pages](docs/GITHUB_PAGES.md)

</div>

## O que e este repo

Uma jornada V1 -> V2 -> V3 de dashboards Plotly/Dash: sunburst hierarquico, filtros em cascata e um dashboard com modelo preditivo linear. Serve como template, guia de boas praticas e registro de debugging de apps Dash.

## Quick start (3 comandos)

    git clone https://github.com/Genovese-Felipe/Python-Data-Driven-Visualization-Journey.git
    cd Python-Data-Driven-Visualization-Journey && pip install -r requirements.txt
    python dashboards/v1_simple/sunburst_cost_explorer_funcional.py   # http://localhost:8052

| Dashboard | Comando | Porta |
|---|---|---|
| V1 Sunburst | python dashboards/v1_simple/sunburst_cost_explorer_funcional.py | 8052 |
| V2 Construcao | python dashboards/v2_construction/V2_script.py | jupyter inline |
| V3 Smart Home | python dashboards/v3_smart_home/Plan_V3_funcional.py | 8053 |

## O que e verdade hoje vs o que nao e

| E verdade | Nao e |
|---|---|
| 3 dashboards Dash funcionais (V1, V2, V3) | dados de producao ou 'reais' — todos os datasets sao sinteticos/hardcoded, rotulados |
| Site estatico no Pages com 4 paginas HTML | dashboards Plotly completos no navegador: paginas index/ dependem de CDN e resumo estatico |
| Modelo linear V3 com R2 in-sample 0,97 (n=10) | analise preditiva robusta: sem holdout, sem validacao |
| CI de testes + Pages check (nesta branch) | garantia de dados reais de construcao |

## Arquitetura em 5 linhas

- dashboards/v1_simple: sunburst hierarquico de custos (dados embutidos no script).
- dashboards/v2_construction: filtros em cascata sobre data.csv (49 linhas, 5 niveis).
- dashboards/v3_smart_home: model.py (LinearRegression) + data.csv (10 linhas) + 4 visualizacoes.
- index/: portfolio estatico publicado no Pages via .github/workflows/pages.yml.
- data/: CSVs compartilhados das versoes raiz (consolidar na Fase 3).

## Testes

    pip install -r requirements.txt && pytest -q

## Roadmap

Ver [auditoria integral](docs/audit/AUDITORIA_INTEGRAL_2026-10-20.md) (matriz P01-P26) e [consolidacao multi-repo](docs/CONSOLIDACAO_MULTI_REPO_2026-10-20.md).

## Licenca

MIT · Felipe de Azevedo Marques Genovese. Imagens de terceiros exigem revisao de procedencia antes de republicacao.
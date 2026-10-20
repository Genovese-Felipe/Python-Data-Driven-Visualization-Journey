# ✦ FGen Data Studio

> **Dados rastreáveis · Dashboards executáveis · GitHub Pages offline · Engenharia de visualização**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3277b3)](https://www.python.org) [![Pages](https://img.shields.io/badge/GitHub%20Pages-Static%20HTML-21b99f)](https://docs.github.com/en/pages) [![Data](https://img.shields.io/badge/Dados-Demonstra%C3%A7%C3%A3o-f5c46c)](docs/audit/IMPLEMENTATION_PLAN.md)

## Três fases da jornada
| Fase | Exploração | Dataset | Formato proposto |
|---|---|---|---|
| **V1** · Hierarquia | Pilares, áreas, serviços e custo | 22 linhas | HTML offline com filtro |
| **V2** · Construção | Budget vs. actual, variância e CSV exportável | 49 linhas | HTML offline com tabelas e filtros |
| **V3** · Smart Home | Custo, economia anual, payback simples | 10 linhas | SVG, scatter, segmentação |
| **Auditoria** | Questões e correções rastreáveis | 21 itens | Matriz em CSV + página HTML |

## Começar
```bash
python scripts/validate_data.py
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/export_portfolio.py --out site
```
Os comandos acima dependem dos arquivos do **pacote de integração completo**, cuja cópia deve ser realizada nesta branch e submetida à revisão antes do merge. O arquivo `README.md` corrente da main permanece intacto.

## Verdades metodológicas
- HTML autossuficiente funciona offline; GitHub Pages **não hospeda callbacks Python de Dash**.
- Os CSVs originais não têm documentação suficiente para reivindicar dados de produção.
- A versão V3 apresenta ajustes de regressão exploratórios com pequena amostra (n=10); não declarar acurácia sem teste fora da amostra.
- O [Predictive Dashboard](https://github.com/Genovese-Felipe/Python-Data-Plotly-Predictive-Analytics-Dashboard) mantém seu próprio Random Forest e dataset sintético; não fundir métricas de um modelo proxy.
- O [Python Data Science Handbook](https://github.com/Genovese-Felipe/PythonDataScienceHandbook) é ligado como fonte externa sob suas licenças; não republicar texto.
- O [monitor eleitoral](https://github.com/carlosduplar/eleicoes-2026-monitor) é estudo separado de qualidade de dados, não fonte para projeções nesta coleção.

## Arquitetura alvo
```text
CSV V1/V2/V3 ──> strict data gate ──> build HTML ──> _site/
                         │               │
                 tests / schema       GitHub Pages
                      AGENTS.md ← portfolio-manifest.json
```

## Auditoria e QA
- [Matriz completa por issue](docs/audit/ISSUE_MATRIX.csv)
- [Inventário estrutural de 1.504 arquivos](docs/audit/FILE_INVENTORY_MULTI_REPO.csv) — **metadados Git, não execução de cada arquivo**.
- [Plano de implementação e rollback](docs/audit/IMPLEMENTATION_PLAN.md)
- [PR #9 preexistente](../../pull/9) — comparar antes de substituir workflow Pages.

## Política de release
Branch de revisão → QA → PR draft → revisão → merge aprovado → Actions deploy. Nada é publicado em produção diretamente nesta branch.

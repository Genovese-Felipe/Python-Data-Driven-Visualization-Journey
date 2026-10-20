<div align="center">

# 📊 Python Data-Driven Visualization Journey

### Da exploração hierárquica ao storytelling e à análise de dados

**Python · Plotly · Dash · HTML offline · Data Analytics**

[🌐 Abrir portfólio estático](https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/) · [📚 Guia de execução](COMO_EXECUTAR.md) · [🧪 Auditoria de revisão](docs/AUDIT_REVISION_2026-10-19.md)

![Python](https://img.shields.io/badge/Python-Data%20Analytics-3776AB?logo=python&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75) ![Dash](https://img.shields.io/badge/Dash-Apps-1E90FF) ![Data](https://img.shields.io/badge/Data-Demonstration-yellow)

</div>

> ⚠️ **Status de revisão:** o repositório contém protótipos demonstrativos. Os dados financeiros e de Smart Home do portfólio são **sintéticos/ilustrativos**. A versão HTML estática não executa um servidor Dash nem um modelo de ML validado.

## Escolha sua experiência

| Etapa | O que demonstra | Executar localmente | Offline HTML |
|:--|:--|:--|:--|
| **V1 — Explore** | Hierarquia e decomposição de custos | `dashboards/v1_simple/` — em saneamento | [Abrir V1](site/dashboard_v1.html) |
| **V2 — Analyze** | Filtros e variação orçamento × realizado | `dashboards/v2_construction/` | [Abrir V2](site/dashboard_v2.html) |
| **V3 — Discover** | Smart Home, dispersão e segmentação | `dashboards/v3_smart_home/` | [Abrir V3](site/dashboard_v3.html) |

## Visualização rápida

![Evolução dos dashboards](assets/screenshots/dashboard_evolution.png)

## Executar (aplicações Dash)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python dashboards/v2_construction/V2_script.py
```

## GitHub Pages

O portfólio de demonstração está em `site/`, com páginas HTML autocontidas e sem bibliotecas remotas. O workflow `.github/workflows/pages.yml` publica `site/` **apenas após merge/revisão na `main`**. É preciso selecionar `Settings → Pages → Source: GitHub Actions`.

A URL acima só estará operacional quando o deploy estiver habilitado e concluído com sucesso.

## Acurácia e limitações

- **V1:** a implementação Python histórica tem tamanhos divergentes entre `labels`, `parents` e `values`; a experiência estática mostra uma reconstrução didática derivada da tabela V2, não o sunburst original.
- **V2:** os 23 registros do HTML são dados ilustrativos, com totais de US$ 4.730.000 realizados e US$ 4.557.000 orçados.
- **V3:** dez registros fictícios; gráficos descritivos não representam performance preditiva validada.

## Próximos marcos

`Audit → Data contracts → V1 fix → Test suite → Responsive QA → Pages → ML validation`

## Licença

MIT — ver [LICENSE](LICENSE).
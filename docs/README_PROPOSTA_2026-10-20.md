# Proposta de README — Python Data Driven Visualization Journey (20/10/2026)

Esta é a proposta de README visual para substituir o atual após aprovação do PR consolidado. Não substitui nada por si só.

---

# 📊 Python Data Driven Visualization Journey
### Portfólio auditável de dashboards interativos — Python · Plotly · Dash

[![CI offline](https://github.com/Genovese-Felipe/Python-Data-Driven-Visualization-Journey/actions/workflows/pages.yml/badge.svg)](../../actions)
[![Licença MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/site-GitHub%20Pages-2ea44f)](https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/)

🇧🇷 Português | 🇺🇸 English below

**Veja agora, sem instalar nada:** os quatro dashboards rodam 100% offline — HTML puro com dados embutidos, sem CDN e sem servidor.

| Dashboard | Tema | Dados |
|---|---|---|
| [V1 · Sunburst](https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/dashboard_v1.html) | Hierarquia de custos | 49 registros reconstruídos |
| [V2 · Engenharia](https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/dashboard_v2.html) | Orçamento x custo x desvio | 49 registros, USD 3.085.000 |
| [V3 · Smart Home](https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/dashboard_v3.html) | Energia e instalações | 10 registros simulados |

## Por que este repositório é diferente

- **Auditável:** cada arquivo tem um parecer na matriz de auditoria (docs/AUDIT_MATRIX.csv).
- **Transparente:** limitações declaradas na própria interface (V1 reconstruída, V2 demonstrativa, V3 simulada).
- **Offline-first:** zero dependência de rede; validação automática de contagens, somas e sintaxe em cada PR.
- **Executável por IA:** agentes autônomos têm contrato explícito em AGENTS.md.

## Início rápido

Abra index.html no navegador. Sem build, sem install.

Para os apps Dash originais (execução externa, não no Pages):

    python -m pip install -r requirements.txt
    python run_app.py

Para validar os HTMLs embutidos:

    python tools/validate_portfolio.py

## Estrutura

    index.html, dashboard_v1-3.html   site estático autocontido (canônico)
    dashboards/                       apps Dash V1-V3 (fonte dos dados)
    docs/                             auditoria, matriz, changelog, guias
    assets/                           imagens de referência
    tools/validate_portfolio.py       validador de integridade
    AGENTS.md                         contrato para agentes de IA

## Iteração contínua

Este portfólio segue um ciclo determinístico: auditar → corrigir dados → regenerar HTML → validar (contagens/somas/JS) → revisar → publicar. Nenhuma publicação ocorre sem CI verde e revisão explícita.

## English

Companion portfolio of three interactive dashboards built with Python, Plotly and Dash, published as fully offline, self-contained HTML. Every file has an audit verdict; every claim is validated by CI. Dash apps run externally; GitHub Pages serves static dashboards only. AI agents: read AGENTS.md first.

---

Licença MIT. Dados demonstrativos; não utilizar em decisões reais sem validação.

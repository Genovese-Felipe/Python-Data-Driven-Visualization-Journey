# AGENTS.md — Contrato de execução para agentes de IA

Este arquivo orienta agentes autônomos (Copilot, Jules, CLIs de IA) a operar neste repositório com segurança.

## Mapa essencial

- index.html, dashboard_v1.html, dashboard_v2.html, dashboard_v3.html: site estático autocontido. CSS, JS, SVG e datasets 100% inline. NÃO carregam recursos externos.
- dashboards/: apps Dash Python (V1-V3) — fonte canônica dos dados.
- tools/validate_portfolio.py: validador determinístico (contagens, somas, paridade, IDs, links, sintaxe JS).
- docs/AUDIT_MATRIX.csv: parecer de auditoria dos 53 arquivos originais.
- docs/CROSS_REVIEW_2026-10-20.md: revisão cross-repo consolidada e plano R0-R5.
- index/: HTMLs legados dependentes de CDN (publicados apenas em /legacy/).

## Dados canônicos (verificados aritmeticamente)

- V2: 49 registros; custo total USD 3.085.000; orçamento USD 2.988.000; desvio USD 97.000.
- V3: 10 registros simulados; soma de Installation_Cost USD 131.500.
- Fonte canônica: implementação Python (dashboards/). Os arrays embutidos nos HTMLs derivam dela.

## Regras

1. NÃO editar manualmente os datasets embutidos nos HTMLs sem atualizar tools/validate_portfolio.py; a validação aritmética falha o CI.
2. NÃO adicionar CDN, scripts externos ou dependências de rede aos quatro HTMLs da raiz.
3. NÃO afirmar ML validado: o modelo V3 foi ajustado em 10 amostras sem avaliação fora da amostra.
4. GitHub Pages publica apenas estático. Apps Dash rodam como processos externos (ex.: python run_app.py), nunca hospedados no Pages.
5. Antes de abrir PR: rodar python tools/validate_portfolio.py e garantir sucesso.
6. Main é protegida por revisão: nunca fazer push direto à main; usar branches review/* + PR.

## Comandos determinísticos

- python tools/validate_portfolio.py  → integridade dos HTMLs (deve terminar com PASS)
- python -m pip install -r requirements.txt && python run_app.py  → apps Dash locais

## Definição de pronto

CI verde (validador), revisão humana aprovada, disclosure de limitações visível na interface, dados conferidos contra a fonte canônica.

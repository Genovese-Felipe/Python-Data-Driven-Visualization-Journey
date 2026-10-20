# Revisão cross-repo consolidada — 20/10/2026

Baseline: main 20486531a623c48e99bf6e529e13c28155b56603. Branch de revisão: review/consolidated-pages-2026-10-20. A main permanece intocada até aprovação do PR.

## 1. Escopo e método

- Três repositórios analisados: Python-Data-Driven-Visualization-Journey (alvo), Python-Data-Plotly-Predictive-Analytics-Dashboard e PythonDataScienceHandbook (contexto e integração).
- Cinco PRs abertos no repositório-alvo inventariados: #7, #9, #10, #11 e #12, com bases divergentes (859aa28, beff5d65 e 2048653).
- Classes de evidência: fonte inspecionada, estrutura de notebook/XML, metadados de imagem, inventário Git e aritmética verificada dos datasets embutidos.
- Verificação aritmética executada nesta revisão: V2 embutida = 49 registros, custo USD 3.085.000, orçamento USD 2.988.000, desvio USD 97.000; V3 embutida = 10 registros, soma de Installation_Cost = 131.500. Confere com tools/validate_portfolio.py.

## 2. Análise cross-repo

| Repositório | Papel | Estado | Principais achados |
|---|---|---|---|
| Python-Data-Driven-Visualization-Journey | Portfólio alvo (V1-V3 + Pages) | main 2048653; 5 PRs abertos sobrepostos | Divergência de bases nos PRs; dois conjuntos de HTML estáticos concorrentes; dataset V2 duplicado com totais distintos; README e docs com claims não verificáveis |
| Python-Data-Plotly-Predictive-Analytics-Dashboard | Dashboard preditivo + Monica AI | main 53a1db0 | Caminho de execução único, dados sintéticos declarados, holdout, pytest e ruff; porém 7 arquivos requirements paralelos, arquivos com sufixos "(1).txt"/"(2).txt" e nomes com espaços |
| PythonDataScienceHandbook | Material de estudo (fork do jakevdp) | fork com .gitmodules | Conteúdo de terceiros: código MIT, texto CC-BY-NC-ND; não é autoria própria e não deve ser republicado como portfólio original |

Decisões cross-repo recomendadas:

- O Journey é o site público canônico do portfólio; o Predictive Analytics entra como case linkado, não como fonte de dados.
- Nenhuma métrica do Predictive Analytics (holdout, atraso) deve ser citada no Journey sem link de proveniência.
- O Handbook permanece material de estudo privado; sem redistribuição do texto (CC-BY-NC-ND).

## 3. Estado dos PRs abertos e destino proposto

| PR | Branch | Base | Conteúdo essencial | Destino proposto |
|---|---|---|---|---|
| #7 | feat/juridical-dashboard | 859aa28 | V4 jurídico Dash (7.561 bytes) | Manter aberto; rebase sobre a main após o merge consolidado; alvo é servidor Dash, não Pages estático |
| #9 | audit/offline-pages-2026-10-19 | 859aa28 | HTMLs offline na raiz, validador, matriz 53 arquivos | Superseded: conteúdo reaplicado nesta branch sobre a main atual |
| #10 | audit/pages-selfcontained-20261019 | 859aa28 | site/ HTMLs, proposta README, static-qa | Superseded: esta branch cobre os mesmos gates com um único workflow |
| #11 | audit/pages-ai-readiness-20261019 | beff5d65 | site/ + catalog.json + CSVs + contratos AI | Superseded: contrato migrado para AGENTS.md desta branch |
| #12 | audit/pages-v4-review-20261019 | 2048653 | pages/ portal + Plotly local + CSVs públicos | Superseded: HTMLs autocontidos eliminam a dependência de bundle Plotly de 4,5MB |

## 4. Conflitos de dados consolidados

| ID | Gravidade | Evidência | Decisão |
|---|---|---|---|
| D1 | Crítica | V1 Python: 97 labels / 97 parents / 53 values | V1 estática reconstruída a partir da V2 canônica; disclosure permanente no HTML |
| D2 | Crítica | index/dashboard_v2.html (23 registros, USD 4.730.000) vs V2 Python (49 registros, USD 3.085.000) | Fonte canônica é a V2 Python; HTML legado vai para /legacy/ com aviso |
| D3 | Crítica | index/dashboard_v3.html com importâncias fixas [0.75, 0.85, 0.15] | Removida a claim de ML validado; V3 rotulada como 10 amostras simuladas |
| D4 | Alta | requirements.txt declara Python 3.12 com NumPy 1.25.2 | Matriz de versões e lock em R1 |
| D5 | Alta | Dois workflows de Pages concorrentes (pages.yml da main + offline-portfolio.yml do PR #9) | Um único workflow pages.yml com validação integrada nesta branch |

## 5. Problemas consolidados e correções (síntese)

A matriz integral dos 53 arquivos está em docs/AUDIT_MATRIX.csv (herdada do PR #9, SHAs preservados). Problemas P0-P3 por tema:

- Dados: D1-D3 acima; geração V3 sem seed (AUDIT_MATRIX: Plan_Data_V3.py).
- Publicação: landing era index/principal.html sem index.html na raiz; CDN plotly-latest obsoleto; Pages não habilitada nas Settings.
- Qualidade de código: run_server(debug=True) em múltiplos apps; testes sem asserts; caminhos absolutos /workspaces/Py_Vy_000; pkill genérico no start_app.sh.
- Documentação: API_REFERENCE.md com símbolos inexistentes; RELEASE_NOTES com claims sem pipeline; notebooks com erros históricos armazenados.
- Ativos: imagens binárias sem manifesto de proveniência/licença; XML de 2,8MB não lido integralmente.

## 6. Arquitetura de publicação decidida nesta branch

- Site canônico: quatro HTMLs autocontidos na raiz (index.html + dashboard_v1/v2/v3.html), inline CSS/JS/SVG/datasets, zero CDN, zero servidor.
- Legacy: index/*.html existentes publicados em /legacy/ para preservação histórica.
- Validação: tools/validate_portfolio.py roda em toda PR e push (contagens, somas, paridade entre as quatro páginas, IDs, links relativos, sintaxe JS via node --check quando disponível).
- Deploy: apenas push na main, via workflow único .github/workflows/pages.yml (atualizado nesta branch).
- V4 jurídico (PR #7): permanece app Dash para execução externa; no site estático entra apenas como link/case, sem backend.

## 7. Plano de implementação

- R0 (esta branch): consolidação, validador, matriz, AGENTS.md, README proposto, workflow único.
- R1: revisar e mesclar este PR; fechar #9-#12 como superseded; habilitar Settings > Pages > Source: GitHub Actions.
- R2: rebase do PR #7 (V4) sobre a nova main; contrato de dados do V4 no mesmo padrão do validador.
- R3: matriz Python (3.11/3.12), lock de dependências, seeds e fixtures CSV versionados, testes pytest reais.
- R4: QA de navegador (Chrome/Firefox/Android), acessibilidade (WCAG), Core Web Vitals, manifesto de proveniência dos ativos binários.
- R5: integração cross-repo: link do Predictive Analytics no README com proveniência; revisão do notebook V006 para currículo reproduzível.

## 8. Executabilidade por IA externa

- AGENTS.md na raiz define mapa do repositório, dados canônicos, comandos e restrições para agentes autônomos.
- Regras: não editar datasets embutidos manualmente (validação aritmética falha); fonte canônica é o Python; nada de claims de ML validado sem holdout documentado; Pages é estático, sem servidor Dash.
- Comandos determinísticos: python tools/validate_portfolio.py (integridade); apps Dash via run_app.py com porta documentada (execução externa, fora do Pages).

## 9. Pendências e limites de evidência

- Pages ainda não habilitada nas Settings; deploy não foi executado nem validado.
- Nenhum teste de navegador real foi executado nesta revisão; JS validado apenas sintaticamente.
- docs/plotly_python_guide.xml (2,8MB) não lido integralmente; imagens binárias inspecionadas só por metadados.
- Testes funcionais, acessibilidade e desempenho permanecem como gates R4 antes de qualquer claim de conformidade.

## 10. Glossário

- CDN: rede de distribuição de conteúdo; dependência externa em tempo de carga.
- Self-contained: arquivo HTML com CSS, JS e dados embutidos, sem recursos externos.
- Holdout: particionamento de dados para avaliação fora da amostra.
- Fixture: dataset versionado e determinístico usado em testes.
- Superseded: PR substituído por outro que cobre o mesmo escopo.
- Baseline: commit de referência sobre o qual a auditoria foi feita.

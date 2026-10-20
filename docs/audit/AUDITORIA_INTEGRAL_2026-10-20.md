# Auditoria Integral — Python-Data-Driven-Visualization-Journey

> Data: 2026-10-20 · Base auditada: main @ 20486531a623c48e99bf6e529e13c28155b56603 (preservada) · Branch de revisao: audit/integral-pages-readme-2026-10-20

## 1. Escopo e metodo

Leitura arquivo por arquivo do caminho canonico (raiz, dashboards/, docs/, index/, data/, tema1/, tema2/, ai_learning_guides/, error_reports/, Plotly_Guides/, .github/, .devcontainer/, assets/) com cruzamento multi-dominio: estrutura/repositorio x codigo Dash x dados/ML x frontend Pages x CI/CD x documentacao x seguranca x consolidacao cross-repo. Calculos deterministicos executados (OLS via equacoes normais, somas de serie) — ver secao 3.

## 2. Inventario por arquivo (sintese)

| Diretorio | Arquivos | Observacoes |
|---|---|---|
| raiz | 18 arquivos | 3 duplicatas divergentes de dashboards/ (drift); 2 scripts teste nao-pytest; 3 notebooks 119-747 KB com outputs |
| dashboards/ | 12 arquivos | v1/v2/v3 canonicos; v3 tem model.py LinearRegression com |coef| nao normalizado |
| docs/ | 9 arquivos | 3 XML totalizando ~4,2 MB versionados; auditoria anterior referencia base 859aa28 (stale) |
| index/ | 4 HTML | plotly-latest.min.js (CDN descontinuado); sunburst com parents como caminhos; KPIs hardcoded divergentes |
| data/ | 3 CSV | sobreposicao com CSVs de dashboards/; schema sem documentacao |
| tema1, tema2 | 2 scripts | gravam HTML na raiz; .gitignore aponta para tema1/*.html (nao bate) |
| ai_learning_guides, error_reports | 3 MD | ok |
| Plotly_Guides | 1 arquivo de 1 byte | nome com typo (XLMextratction) |
| .github/workflows | pages.yml | deploy Pages correto (Actions-based); sem CI de testes |
| .devcontainer | devcontainer.json 55 B | sem postCreateCommand |
| assets | 5 arquivos | imagens de referencia existem (3) + 1 screenshot |

## 3. Evidencias deterministicas

- dashboard_v1.html: serie embutida com 53 valores, soma = US$ 11.575.000; card KPI afirma US$ 10,8M (+7,2% de divergencia). Maior valor da serie = US$ 2.025.000; card afirma maior custo individual US$ 600K. Ambos os KPIs estao errados (P06).
- Rotulo 'MarchJEP Engineering' presente em dashboard_v1.html (typo; ME(?) Engineering esperado).
- V3 OLS (n=10, in-sample): R2 = 0,970. Ranking bruto |coef|: Satisfaction 245,1 > Cost 171,9 > Devices 151,5. Ranking com coeficientes padronizados: Cost 1,31 > Devices 0,59 > Satisfaction 0,086. O ranking do repo (bruto) esta invertido em relacao ao ranking justo (P12).
- V2 data.csv: 49 linhas, custo total US$ 3.085.000, orcamento US$ 2.988.000, variancia +3,25%. Por pilar: Construction 2.025.000; Management 405.000; Finishing & Landscaping 340.000; Project Design 315.000.
- index/*.html carregam https://cdn.plot.ly/plotly-latest.min.js — endpoint descontinuado pela Plotly; risco de renderizar apenas o placeholder (P04).
- dashboard_v1.html monta sunburst com parents = caminhos completos 'A/B/C/D' que nao correspondem a nenhum label; com branchvalues:'total' os setores ficam orfaos e o grafo hierarquico nao se forma (P05).

## 4. Matriz de problemas (P01-P26)

| ID | Grav | Dominio | Arquivo(s) | Problema | Correcao proposta | Fase |
|---|---|---|---|---|---|---|
| P01 | Critica | Deps/CI | requirements.txt | numpy==1.25.2 nao tem wheels p/ Python 3.12 exigido pelo README; install quebra | numpy==1.26.4 (aplicado nesta branch) | 1 |
| P02 | Critica | CI | .github/ | Sem workflow de testes; pytest declarado e nunca executado; test_*.py sao scripts sem assert | ci.yml + tests/test_smoke.py (aplicado nesta branch) | 1 |
| P03 | Critica | Codigo | test_app.py | sys.path.append('/workspaces/Py_Vy_000') hardcoded quebra fora do codespace antigo | remover path e converter em teste real (aplicado nesta branch) | 1 |
| P04 | Critica | Pages | index/*.html | CDN plotly-latest.min.js descontinuado; dashboards podem renderizar placeholder | fixar versao: plotly-2.35.2.min.js; guard no CI | 2 |
| P05 | Alta | Pages | index/dashboard_v1.html | parents do sunburst sao caminhos, nao labels; hierarquia orfa | reconstruir com uma linha por nivel (id/parent/value) | 2 |
| P06 | Alta | Dados/Web | index/dashboard_v1.html | KPIs hardcoded divergem da serie (+7,2%; max 2.025.000 vs 600K); typo MarchJEP | computar KPIs dos dados; teste de soma no CI | 1-2 |
| P07 | Alta | Estrutura | raiz vs dashboards/ | duplicatas divergentes (sunburst 14.682 vs 14.966 B; Plan_V3 11.005 vs 12.207 B) | canonico = dashboards/; arquivar raiz em legacy/ | 2 |
| P08 | Alta | Estrutura | raiz | notebooks de 747/165/119 KB com outputs na raiz | mover p/ notebooks/ e limpar outputs | 2 |
| P09 | Alta | Estrutura | docs/*.xml | 4,2 MB de XML versionados inflando clone | docs/guides/ + Git LFS ou release asset | 2 |
| P10 | Alta | Docs | README.md | overclaim ('dados reais', 'Status: Complete') e duplicacao PT/EN integral | README.proposed.md com tabela verdade (nesta branch) | 2 |
| P11 | Alta | Docs | README.md x README_VISUAL_PROPOSTA.md | dois READMEs concorrentes, badges 3.12 x 3.11 | consolidar no proposto | 2 |
| P12 | Alta | ML | dashboards/v3_smart_home/model.py | n=10 sem holdout; importance=|coef| bruto (ranking invertido comprovado) | StandardScaler + permutation importance; disclaimer toy | 2 |
| P13 | Media | Codigo | dashboards/v2_construction/V2_script.py | jupyter_mode='inline' exige jupyter-dash (ausente) | dep adicionada nesta branch ou app.run padrao | 1 |
| P14 | Media | Estrutura | .gitignore | linha 1 orfa; tema1/*.html nao cobre outputs reais (raiz); lib/,parts/ perigosos | limpar e corrigir padroes | 3 |
| P15 | Media | Codigo | start_app.sh | shebang fora da 1a linha; sugere pkill -f python | shebang na linha 1; kill por PID | 3 |
| P16 | Media | Estrutura | .devcontainer/devcontainer.json | sem postCreateCommand (deps nao instalam) | completar JSON | 3 |
| P17 | Media | Codigo | app_simples.py, run_app.py | colisao de portas 8050 (e V1 8052, V3 8053) | mapa de portas unico documentado | 3 |
| P18 | Media | Repositorio | branches | 18 branches acumuladas (7 audit, 6 review, 2 copilot, codespace, feat, docs) | deletar pos-merge; protection na main | 3 |
| P19 | Media | CI | .github/workflows/pages.yml | valida presenca mas nao links nem consistencia de dados | link-check + schema check no ci.yml (aplicado) | 1 |
| P20 | Media | Pages | index/ | sem 404.html, robots.txt, favicon | adicionar ao _site no workflow | 3 |
| P21 | Baixa | Estrutura | Plotly_Guides/About_Guides_XLMextratction.md | 1 byte, nome com typo | preencher ou remover | 3 |
| P22 | Baixa | Docs | docs/AUDITORIA_PAGES_2026-10-19.md | referencia base 859aa28 (main ja em 2048653) | auditorias versionadas em docs/audit/ (aplicado) | 1 |
| P23 | Baixa | Dados | data/, scripts | 4+ CSVs sobrepostos e dados hardcoded nos scripts | fonte unica data/ + schema.md | 3 |
| P24 | Baixa | Seguranca | repo | sem SECURITY.md (nenhum segredo encontrado nos arquivos lidos) | adicionar SECURITY.md leve | 3 |
| P25 | Info | Cross-repo | PythonDataScienceHandbook | fork (texto CC-BY-NC-ND) — nao copiar texto em repos proprios | usar como referencia apenas | — |
| P26 | Info | Cross-repo | Journey + Plotly Predictive | consolidacao num hub Pages unico com dashboards self-contained e AI-executaveis | ver docs/CONSOLIDACAO_MULTI_REPO_2026-10-20.md | 4 |

## 5. Plano de implementacao (nesta branch, main preservada)

### Fase 1 — ja aplicado nesta branch

- docs/audit/AUDITORIA_INTEGRAL_2026-10-20.md (este documento)
- README.proposed.md (README visual, honesto e iterativo)
- docs/GITHUB_PAGES.md (receita de publicacao)
- docs/CONSOLIDACAO_MULTI_REPO_2026-10-20.md (cruzamento dos 3 repos)
- .github/workflows/ci.yml (testes 3.11/3.12 + guard de CDN/Pages)
- tests/test_smoke.py + test_app.py corrigido (P03)
- requirements.txt corrigido (P01, P13)
- index/audit_hub.html (dashboard de auditoria self-contained, zero dependencias)

### Fase 2 — apos revisao (PR para main)

- Fix CDN plotly-2.35.2 nos 4 index/*.html (P04)
- Reconstruir hierarquia do sunburst (P05) e computar KPIs (P06)
- Promover README.proposed.md a README.md; arquivar duplicatas da raiz em legacy/ (P07)
- Mover notebooks p/ notebooks/ com outputs limpos (P08); XML p/ LFS (P09)
- model.py: scaler + permutation importance + holdout (P12)

### Fase 3 — higiene

- .gitignore, start_app.sh, devcontainer, portas, 404/robots, SECURITY.md, branches stale

### Fase 4 — consolidacao cross-repo

- Hub publico unico (ver doc de consolidacao); dados reais somente quando houver fonte citada.

## 6. Riscos e limitacoes

Aplicacoes Dash nao foram executadas nesta auditoria (analise estatica + dados). Guia XML/imagens inventariados, nao validados semanticamente. Soma da serie V1 recomputada de codigo-fonte; se a intencao era hierarquia agregada, a duplicacao folha+agregado na serie embutida precisa ser resolvida na Fase 2 (P05/P06).
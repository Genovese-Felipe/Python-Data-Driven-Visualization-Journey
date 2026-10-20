# Inventário de auditoria e matriz de correções (main 859aa2882b29)

**Escopo:** 53 arquivos versionados. **Status:** inspeção estática e cruzamento de metadados; não há certificação de execução integral dos 53 arquivos. **Validação parcial:** 4 imagens revisadas apenas como objetos Git; `docs/plotly_python_guide.xml` excedeu a janela de extração textual; notebooks foram analisados estruturalmente, não executados de ponta a ponta.

## Resumo executivo

1. **Bloqueador V1:** 97 rótulos e 97 relações de parentesco para somente 53 valores no Python. Reconstruir árvore, usar IDs únicos, conferir relações e modelo `branchvalues`.
2. **Bloqueador V2:** 49 registros Python somam **US$ 3.085.000** (`budgeted_cost` = **US$ 2.988.000**); o HTML legado soma **US$ 4.730.000** em 23 registros. Diferença de **US$ 1.645.000**. O novo HTML usa dados fonte Python e IDs estáveis.
3. **V3/ML:** regressão `LinearRegression` treinada com 10 linhas; importância baseada em `abs(coef_)` sem escalas comparáveis; ausência de validação externa. Publicar somente como demonstração.
4. **Pages:** faltava arquivo `index.html` na raiz; site legado depende de CDN `plotly-latest`. Criado `index.html` autónomo sem CDN na branch.
5. **Automação:** adicionados contratos JSON, teste de paridade Python e workflow GitHub Pages, para *depois* de revisão e merge.
6. **Segurança/portabilidade:** debugs legados em rede e caminhos absolutos; não hospedar o servidor Dash no Pages.

### Arquivo por arquivo

| Arquivo | Prioridade | Inspeção | Achado resumido |
|---|---|---|---|
| `.devcontainer/devcontainer.json` | P2 | static source inspected | Ambiente de desenvolvimento mínimo; reprodutibilidade não demonstrada |
| `.gitignore` | P3 | static source inspected | Configuração histórica; cobertura de temporários a revisar |
| `COMO_EXECUTAR.md` | P2 | static source inspected | Exemplos de inicialização desatualizados e sem política estática |
| `LICENSE` | P3 | static source inspected | Licença-fonte presente; proveniência das imagens/dados não esclarecida |
| `Plan_Data_V3.py` | P2 | static source inspected | Geração aleatória sem seed fixa |
| `Plan_V3_funcional.py` | P1 | static source inspected | 10 observações; regressão treinada in-sample; sem validação |
| `Plotly_Guides/About_Guides_XLMextratction.md` | P3 | static source inspected | Arquivo de 1 byte vazio na prática |
| `Python_colab_tutorial_Part_1_V001.ipynb` | P2 | static source inspected | 214 células, 1 saída de erro histórica |
| `README.md` | P1 | static source inspected | Declarações de dados reais vs exemplos não auditados; texto extenso duplicado |
| `RELATORIO_MELHORIAS.md` | P2 | static source inspected | Promessas de operação não vinculadas à execução CI atual |
| `RELEASE_NOTES.md` | P2 | static source inspected | Notas 2025 declaram 3/3 completos e reais |
| `ai_learning_guides/effective_prompt_engineering.md` | P2 | static source inspected | Recomendações de dados reais sem dataset público comprovado |
| `ai_learning_guides/plotly_dash_best_practices.md` | P2 | static source inspected | Boas práticas nem sempre refletidas nos scripts históricos |
| `app_simples.py` | P2 | static source inspected | Rota de inicialização legada run_server(debug=True) |
| `assets/README.md` | P2 | static source inspected | Descrição de imagens sem manifest/licença/hash |
| `assets/reference_images/Imagem_Referencia_1.png` | P2 | git-object/size only | Imagem presente; conteúdo binário não inspecionado visualmente |
| `assets/reference_images/Imagem_Referencia_2.jpg` | P2 | git-object/size only | Imagem presente; conteúdo binário não inspecionado visualmente |
| `assets/reference_images/Imagem_Referencia_3.png` | P2 | git-object/size only | Imagem presente; conteúdo binário não inspecionado visualmente |
| `assets/screenshots/dashboard_evolution.png` | P2 | git-object/size only | Screenshot presente; sem validação visual no ciclo atual |
| `dashboards/v1_simple/README.md` | P1 | static source inspected | Afirma dados reais embora origem pareça referência HTML |
| `dashboards/v1_simple/sunburst_cost_explorer_funcional.py` | P0 | static source inspected | 97 labels e parents, 53 values; modelagem hierárquica inconsistente |
| `dashboards/v2_construction/README.md` | P2 | static source inspected | Descrição de filtros sem teste de integração atual |
| `dashboards/v2_construction/V2_script.py` | P1 | static source inspected | 49 itens canônicos, custo total 3.085.000, orçamento 2.988.000; diverge HTML |
| `dashboards/v3_smart_home/Plan_Data_V3.py` | P2 | static source inspected | Duplicata byte a byte do Plan_Data_V3.py da raiz |
| `dashboards/v3_smart_home/Plan_V3.py` | P1 | static source inspected | Trata colunas contínuas como categorias e pressupõe df_complex externo |
| `dashboards/v3_smart_home/Plan_V3.txt` | P2 | static source inspected | Texto de planejamento/rascunhos não é módulo executável |
| `dashboards/v3_smart_home/Plan_V3_funcional.py` | P1 | static source inspected | 10 observações e 'feature importance' por coeficientes absolutos sem padronização |
| `dashboards/v3_smart_home/README.md` | P1 | static source inspected | Promete ML preditivo sem métricas de generalização |
| `docs/API_REFERENCE.md` | P1 | static source inspected | Nomes de funções no guia sem correspondência comprovada |
| `docs/CHANGELOG.md` | P2 | static source inspected | Histórico de correções não alinhado a scripts legados |
| `docs/CONTRIBUTING.md` | P2 | static source inspected | Critérios de contribuição sem checks automatizados obrigatórios |
| `docs/advanced_pedagogical_plotly_guide.xml` | P3 | static source inspected | XML extenso; inspecionado textualmente sem validar todas referências |
| `docs/plotly_python_guide.xml` | P2 | content unavailable API size limit | 2,82MB: extração pela API excedeu limite; não houve leitura integral |
| `docs/semantic_plotly_guide.xml` | P3 | static source inspected | XML extenso, sem verificação de cada código exemplo |
| `docs/technical_documentation.md` | P2 | static source inspected | Estimativas de produção sem benchmark e comando gunicorn a conferir |
| `docs/visual_journey.md` | P2 | static source inspected | Evolução visual depende de captura de tela histórica |
| `error_reports/complete_error_analysis.md` | P2 | static source inspected | Erros históricos documentados; falta vínculo com regressão automatizada |
| `index/dashboard_v1.html` | P0 | static source inspected | CDN plotly-latest; dados reduzidos e script de fallback antes do DOM |
| `index/dashboard_v2.html` | P0 | static source inspected | 23 agregados somam 4.730.000 contra 3.085.000 no Python |
| `index/dashboard_v3.html` | P1 | static source inspected | 10 dados sintéticos e claims preditivos sem modelo executado no browser |
| `index/principal.html` | P1 | static source inspected | É portal mas não index.html na raiz; links relativos de pasta |
| `python-colab.ipynb` | P2 | static source inspected | 180 células; 2 saídas de erro históricas, 84 outputs e 0 contadores de execução |
| `requirements.txt` | P1 | static source inspected | Pinos 2023/2024 e conflito com guia Python 3.12 a verificar |
| `run_app.py` | P1 | static source inspected | debug=True em 0.0.0.0 com run_server legada |
| `start_app.sh` | P1 | static source inspected | Caminho absoluto /workspaces/Py_Vy_000 e ambiente não portátil |
| `sunburst_app_simples_funcionando.py` | P2 | static source inspected | Múltiplas versões e debug=True sem suíte de regressão |
| `sunburst_cost_explorer_app.py` | P1 | static source inspected | Módulo amplo 790 linhas e múltiplas responsabilidades |
| `sunburst_cost_explorer_funcional.py` | P2 | static source inspected | Versão paralela potencialmente divergente da V1 |
| `tema1/chart1.py` | P2 | static source inspected | Gráficos de vendas usam dados fictícios |
| `tema2/chart2.py` | P2 | static source inspected | Gráficos financeiros usam dados fictícios |
| `test_app.py` | P1 | static source inspected | sys.path fixo para /workspaces/Py_Vy_000; smoke print não automatizado |
| `test_dash_simple.py` | P2 | static source inspected | É um aplicativo Dash de exemplo, não um teste de CI |
| `v006_rvw.ipynb` | P1 | static source inspected | 237 células; 3 saídas de erro; 21 callbacks históricos, notebook grande |

## Etapas e critérios de aceitação

| Gate | Requisito | Prioridade |
|---|---|---|
| G0 | Não modificar `main`; PR em draft; preservar conteúdo original | P0 |
| G1 | 49 linhas V2, 10 V3, paridade inline/JSON, 3.085.000 / 2.988.000 | P0 |
| G2 | HTML sem JS remoto, abas/filtros/CSV operacionais e mobile/keyboard | P0 |
| G3 | Publicar apenas conteúdo sem dados pessoais, segredos ou imagens sem licença | P1 |
| G4 | CI bem-sucedido no PR; cobertura de código Python legados antes de marcá-los funcionais | P1 |
| G5 | Revisar README, modelos ML e notebooks; proteção `main` | P1 |
| G6 | Só publicar após merge e configurar Settings → Pages → GitHub Actions | P0 |

## Testes executados e limites

- Inspeção por GitHub API de 49 arquivos de texto e metadados de 4 mídias; conteúdo XML de 2.82 MB não extraído por limite.
- Notebook `Python_colab_tutorial_Part_1_V001.ipynb`: 214 células / 1 output de erro; `python-colab.ipynb`: 180 / 2 erros; `v006_rvw.ipynb`: 237 / 3 erros.
- HTML offline anterior (artefato local separado): teste funcional Chromium em quatro variantes, filtros, abas e JavaScript sem exceções.
- **Ainda não executado:** build GitHub Actions da branch, revisão visual das imagens, execução Dash Python com suas dependências, deploy Pages real e auditoria dinâmica de acessibilidade.
- O código e datasets enviados à branch são propostas de revisão, não mudanças incorporadas à `main`.

## Próximas entregas recomendadas

1. CI no PR e revisão dos dados; corregir erros se necessário.
2. Refatorar V1 de `labels/parents/values` para uma tabela de nós única.
3. Consolidar V2 Python e HTML usando `data/construction_v2.json` como entrada (ou gerar JSON da fonte).
4. Definir protocolo de avaliação ML no V3 com divisão temporal/LOOCV e baseline — sem promessas comerciais.
5. Arquivar exemplos históricos e registrar proveniência/licenciamento dos assets.

# Inventário rastreável — auditoria arquivo a arquivo

Base: `main@859aa2882b290268d46d7027b4eb437cb844914b`. 53 blobs, árvore não truncada. As classificações `INS` denotam inventário com metadados, **não** execução nem validação do conteúdo integral. P0/P1/P2 são achados direcionados. OBS indica leitura parcial. Imagens: somente metadados; XML: leitura inicial/parcial. 

| Arquivo | Tamanho | Domínio | Achado | Próxima ação |
|---|---:|---|---|---|
| `.devcontainer/devcontainer.json` | 55 B | Configuração/outros | **P2**: Imagem não garante dependências instaladas | Adicionar postCreateCommand |
| `.gitignore` | 429 B | Configuração/outros | **INS**: Somente inventário/inspeção preliminar | Validar em revisão CI |
| `COMO_EXECUTAR.md` | 4.8 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `LICENSE` | 1.1 KB | Configuração/outros | **INS**: Somente inventário/inspeção preliminar | Validar em revisão CI |
| `Plan_Data_V3.py` | 2.2 KB | Python | **P1**: Cópia idêntica de Plan_Data_V3.py do dashboard | Usar única implementação |
| `Plan_V3_funcional.py` | 10.7 KB | Python | **INS**: Somente inventário/inspeção preliminar | AST, lint, import e testes unitários |
| `Plotly_Guides/About_Guides_XLMextratction.md` | 1 B | Documentação | **P2**: Arquivo quase vazio (1 byte) | Documentar origem ou eliminar link |
| `Python_colab_tutorial_Part_1_V001.ipynb` | 116.5 KB | Notebooks | **P2**: 214 células e 29 outputs salvos | Testar execução incremental |
| `README.md` | 16.7 KB | Documentação | **P1**: Declarações de status completo sem CI validada | Evidências e matriz de maturidade |
| `RELATORIO_MELHORIAS.md` | 8.6 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `RELEASE_NOTES.md` | 9.2 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `ai_learning_guides/effective_prompt_engineering.md` | 6.6 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `ai_learning_guides/plotly_dash_best_practices.md` | 10.0 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `app_simples.py` | 4.2 KB | Python | **P1**: Servidor debug exposto em 0.0.0.0 | Parametrizar bind e debug |
| `assets/README.md` | 2.1 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `assets/reference_images/Imagem_Referencia_1.png` | 194.1 KB | Imagens | **INS**: Somente inventário/inspeção preliminar | Analisar conteúdo visual, licenças e alt text |
| `assets/reference_images/Imagem_Referencia_2.jpg` | 70.8 KB | Imagens | **INS**: Somente inventário/inspeção preliminar | Analisar conteúdo visual, licenças e alt text |
| `assets/reference_images/Imagem_Referencia_3.png` | 1184.6 KB | Imagens | **INS**: Somente inventário/inspeção preliminar | Analisar conteúdo visual, licenças e alt text |
| `assets/screenshots/dashboard_evolution.png` | 798.7 KB | Imagens | **INS**: Somente inventário/inspeção preliminar | Analisar conteúdo visual, licenças e alt text |
| `dashboards/v1_simple/README.md` | 1.3 KB | Dashboards Python/docs | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `dashboards/v1_simple/sunburst_cost_explorer_funcional.py` | 13.3 KB | Dashboards Python/docs | **P0**: 97 labels, 97 parents, 53 values; soma hierárquica potencialmente duplicada | Revalidar dataset e métricas folha |
| `dashboards/v2_construction/README.md` | 2.3 KB | Dashboards Python/docs | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `dashboards/v2_construction/V2_script.py` | 15.8 KB | Dashboards Python/docs | **INS**: Somente inventário/inspeção preliminar | AST, lint, import e testes unitários |
| `dashboards/v3_smart_home/Plan_Data_V3.py` | 2.2 KB | Dashboards Python/docs | **P1**: Dados gerados aleatoriamente, cópia idêntica na raiz | Unificar e fixar semente |
| `dashboards/v3_smart_home/Plan_V3.py` | 9.0 KB | Dashboards Python/docs | **P0**: Referência a df_complex sem definição no módulo | Criar import explícito de fonte canônica |
| `dashboards/v3_smart_home/Plan_V3.txt` | 15.1 KB | Dashboards Python/docs | **INS**: Somente inventário/inspeção preliminar | Validar em revisão CI |
| `dashboards/v3_smart_home/Plan_V3_funcional.py` | 11.0 KB | Dashboards Python/docs | **INS**: Somente inventário/inspeção preliminar | AST, lint, import e testes unitários |
| `dashboards/v3_smart_home/README.md` | 3.5 KB | Dashboards Python/docs | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `docs/API_REFERENCE.md` | 12.3 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `docs/CHANGELOG.md` | 6.0 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `docs/CONTRIBUTING.md` | 8.8 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `docs/advanced_pedagogical_plotly_guide.xml` | 400.4 KB | XML/Guias | **OBS**: Cabeçalho inspecionado; corpo XML não validado | Validar XSD e estrutura no pipeline |
| `docs/plotly_python_guide.xml` | 2755.3 KB | XML/Guias | **OBS**: 2,8 MB, cabeçalho não recuperado no recorte solicitado | Validar XML via parser local no pipeline |
| `docs/semantic_plotly_guide.xml` | 955.2 KB | XML/Guias | **OBS**: Cabeçalho inspecionado; corpo XML não validado | Validar XSD e estrutura no pipeline |
| `docs/technical_documentation.md` | 5.8 KB | Documentação | **P1**: Exemplo Gunicorn publica Dash app não WSGI server | Ajustar :server |
| `docs/visual_journey.md` | 6.2 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `error_reports/complete_error_analysis.md` | 7.5 KB | Documentação | **INS**: Sem anomalia crítica confirmada nesta passagem | Validar em revisão CI |
| `index/dashboard_v1.html` | 17.0 KB | HTML legado | **P1**: Plotly remoto plotly-latest | Usar export offline versionado |
| `index/dashboard_v2.html` | 21.5 KB | HTML legado | **P1**: KPI inicial $2.5M inconsistente com dataset | Calcular por base única |
| `index/dashboard_v3.html` | 24.3 KB | HTML legado | **P0**: ML hardcoded + dependência de CDN/map tiles | Rotular demo, cálculo validado, eliminar rede |
| `index/principal.html` | 12.0 KB | HTML legado | **P2**: Entrada aninhada em index/, sem raiz index.html | Reestruturar origem Pages |
| `python-colab.ipynb` | 161.6 KB | Notebooks | **P2**: 180 células, 86 outputs armazenados | Sanear outputs e dependências |
| `requirements.txt` | 314 B | Configuração/outros | **P1**: Pins antigos e mistura runtime/desenvolvimento | Atualizar compatibilidade com CI |
| `run_app.py` | 6.7 KB | Python | **P1**: Servidor debug exposto em 0.0.0.0 | Parametrizar bind e debug |
| `start_app.sh` | 840 B | Shell | **P1**: shebang não é primeira linha; pkill amplo; caminho absoluto | Shellcheck, corrigir PID e venv |
| `sunburst_app_simples_funcionando.py` | 14.1 KB | Python | **INS**: Somente inventário/inspeção preliminar | AST, lint, import e testes unitários |
| `sunburst_cost_explorer_app.py` | 29.1 KB | Python | **INS**: Somente inventário/inspeção preliminar | AST, lint, import e testes unitários |
| `sunburst_cost_explorer_funcional.py` | 12.8 KB | Python | **INS**: Somente inventário/inspeção preliminar | AST, lint, import e testes unitários |
| `tema1/chart1.py` | 3.4 KB | Python | **P2**: Script fig.show() / efeitos colaterais ao executar | Proteger entradas e exportar via CLI |
| `tema2/chart2.py` | 6.4 KB | Python | **P2**: Script fig.show() / efeitos colaterais ao executar | Proteger entradas e exportar via CLI |
| `test_app.py` | 956 B | Python | **P2**: Smoke dependente de import de app, sem asserts sistemáticos | Reescrever pytest |
| `test_dash_simple.py` | 508 B | Python | **P1**: Script teste inicia servidor debug; não é teste automatizado | Separar smoke de pytest |
| `v006_rvw.ipynb` | 729.7 KB | Notebooks | **P2**: 237 células, 20 outputs armazenados; reproducibilidade não comprovada | Executar notebook CI com dados fixos |

## Próximas validações automatizadas

- Lint AST, `python -m compileall`, Ruff/Black e Bandit em scripts Python.
- Reprocessamento de notebooks com nbclient/papermill e bloqueio de outputs excessivos.
- XML com `xml.etree.ElementTree` e checks de integridade.
- Testes E2E de filtros e layout (mobile/desktop) + offline com rede bloqueada.
- Responsividade, contraste WCAG e screen reader.
- Dependabot/pip-audit e proveniência dos dados.

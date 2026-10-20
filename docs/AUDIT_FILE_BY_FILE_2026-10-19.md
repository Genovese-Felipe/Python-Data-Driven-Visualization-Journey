# Auditoria por arquivo — árvore main (19/10/2026)

**Escopo**: 56 blobs; árvore integral via GitHub REST `/git/trees/main?recursive=1`. Este documento é uma **triagem integral de inventário** com inspeção de código e documentação prioritários. *Não representa execução de todas as células, leitura de todos os XMLs de megabytes ou inspeção pixel a pixel de imagens.* Indicações `P0` são bloqueadoras. Nem todos os achados são bugs comprovados; os itens apenas inventariados exigem validação.

| Nº | Arquivo | Bytes | Prioridade | Evidência / condição | Ação de revisão |
|---:|---|---:|---|---|---|
| 1 | `.devcontainer/devcontainer.json` | 55 | P2 | Imagem devcontainer universal sem lock. | Fixar runtime quando o ambiente CI estiver estabilizado. |
| 2 | `.github/workflows/pages.yml` | 1,734 | P2 | Arquivo catalogado; verificação detalhada de comportamento pendente. | Preservar, estabelecer testes/evidência e manter vínculo com objetivo. |
| 3 | `.gitignore` | 429 | P2 | Exclui outputs temporários mas não define política para builds Pages. | Distinguir saídas versionadas de produtos gerados no CI. |
| 4 | `ai_learning_guides/effective_prompt_engineering.md` | 6,718 | P2 | Guia de IA; exemplos misturam APIs históricas. | Sincronizar instruções com testes executáveis. |
| 5 | `ai_learning_guides/plotly_dash_best_practices.md` | 10,254 | P2 | Guia de IA; exemplos misturam APIs históricas. | Sincronizar instruções com testes executáveis. |
| 6 | `app_simples.py` | 4,292 | P1 | Uso legado de run_server e callbacks. | Fixar API de Dash e testar cold start. |
| 7 | `assets/README.md` | 2,157 | P2 | Metadados de recursos e documentação de galeria. | Verificar atribuição e proveniência das imagens. |
| 8 | `assets/reference_images/Imagem_Referencia_1.png` | 198,728 | P2 | Imagem binária catalogada por caminho/tamanho; pixels não revisados. | Validar correspondência visual, alt text e licenças manualmente. |
| 9 | `assets/reference_images/Imagem_Referencia_2.jpg` | 72,509 | P2 | Imagem binária catalogada por caminho/tamanho; pixels não revisados. | Validar correspondência visual, alt text e licenças manualmente. |
| 10 | `assets/reference_images/Imagem_Referencia_3.png` | 1,212,988 | P2 | Imagem binária catalogada por caminho/tamanho; pixels não revisados. | Validar correspondência visual, alt text e licenças manualmente. |
| 11 | `assets/screenshots/dashboard_evolution.png` | 817,918 | P2 | Imagem binária catalogada por caminho/tamanho; pixels não revisados. | Validar correspondência visual, alt text e licenças manualmente. |
| 12 | `COMO_EXECUTAR.md` | 4,869 | P1 | Inspecionado: referências repetidas a /workspaces/... e servidor local. | Reescrever comandos para clone comum e distinção Pages/Dash. |
| 13 | `dashboards/v1_simple/README.md` | 1,340 | P1 | README de versão inspecionado. | Atualizar instruções com comandos testados e dados sintéticos. |
| 14 | `dashboards/v1_simple/sunburst_cost_explorer_funcional.py` | 13,613 | P0 | Inspecionado: 97 IDs/parents vs 53 valores, 45 cores, parents não resolvidos. | Substituir arrays paralelos por registros folha; validar árvore. |
| 15 | `dashboards/v2_construction/README.md` | 2,305 | P1 | README de versão inspecionado. | Atualizar instruções com comandos testados e dados sintéticos. |
| 16 | `dashboards/v2_construction/V2_script.py` | 16,164 | P0 | Inspecionado: 49 folhas, custo 3.085.000; hover aritmético inválido e modo inline. | Pré-calcular variance, validar dropdowns e totalização. |
| 17 | `dashboards/v3_smart_home/Plan_Data_V3.py` | 2,216 | P2 | Fixture do V3; 10 amostras simuladas. | Declarar dataset sintético e esquema. |
| 18 | `dashboards/v3_smart_home/Plan_V3_funcional.py` | 11,295 | P1 | Inspecionado: apenas 10 linhas simuladas e regressão treinada sem holdout. | Marcar demonstração sem acurácia e usar avaliação real para ML. |
| 19 | `dashboards/v3_smart_home/Plan_V3.py` | 9,228 | P1 | App alternativo obsoleto usa run_server. | Marcar legado e migrar execução à entrada canônica. |
| 20 | `dashboards/v3_smart_home/Plan_V3.txt` | 15,466 | P2 | Arquivo catalogado; verificação detalhada de comportamento pendente. | Preservar, estabelecer testes/evidência e manter vínculo com objetivo. |
| 21 | `dashboards/v3_smart_home/README.md` | 3,604 | P1 | README de versão inspecionado. | Atualizar instruções com comandos testados e dados sintéticos. |
| 22 | `docs/advanced_pedagogical_plotly_guide.xml` | 409,996 | P2 | Guia XML grande; metadata inventariada, não renderizada/executada. | Validar licença, tamanho, links e mover documentação pesada para release quando apropriado. |
| 23 | `docs/API_REFERENCE.md` | 12,621 | P2 | Documentação inspeccionada por cabeçalhos e referências. | Conferir promessas vs código e links relativos. |
| 24 | `docs/AUDITORIA_PAGES_2026-10-19.md` | 5,965 | P2 | Documentação inspeccionada por cabeçalhos e referências. | Conferir promessas vs código e links relativos. |
| 25 | `docs/CHANGELOG.md` | 6,115 | P2 | Documentação inspeccionada por cabeçalhos e referências. | Conferir promessas vs código e links relativos. |
| 26 | `docs/CONTRIBUTING.md` | 9,043 | P2 | Documentação inspeccionada por cabeçalhos e referências. | Conferir promessas vs código e links relativos. |
| 27 | `docs/plotly_python_guide.xml` | 2,821,462 | P2 | Guia XML grande; metadata inventariada, não renderizada/executada. | Validar licença, tamanho, links e mover documentação pesada para release quando apropriado. |
| 28 | `docs/semantic_plotly_guide.xml` | 978,131 | P2 | Guia XML grande; metadata inventariada, não renderizada/executada. | Validar licença, tamanho, links e mover documentação pesada para release quando apropriado. |
| 29 | `docs/technical_documentation.md` | 5,940 | P2 | Documentação inspeccionada por cabeçalhos e referências. | Conferir promessas vs código e links relativos. |
| 30 | `docs/visual_journey.md` | 6,306 | P2 | Documentação inspeccionada por cabeçalhos e referências. | Conferir promessas vs código e links relativos. |
| 31 | `error_reports/complete_error_analysis.md` | 7,665 | P2 | Histórico de falhas diagnosticadas. | Marcar correção verificada versus relato antigo. |
| 32 | `index/dashboard_v1.html` | 17,431 | P0 | Inspecionado: 53 parents não correspondem a labels; card estático divergente. | Regenerar HTML por pipeline a partir do V2 auditado; não declarar restauração fiel. |
| 33 | `index/dashboard_v2.html` | 22,055 | P0 | Inspecionado: 23 linhas independentes do Python V2; total distinto. | Gerar HTML da mesma fonte de dados versionada. |
| 34 | `index/dashboard_v3.html` | 24,832 | P1 | HTML com dependência de CDN plotly-latest e KPIs estáticos. | Gerar snapshot embutido e conferir dados com Plan_V3. |
| 35 | `index/principal.html` | 12,289 | P1 | Landing histórico, links relativos para dashboards legados. | Renovar galeria e indicar fonte, limitações e execução. |
| 36 | `LICENSE` | 1,091 | P2 | Licença MIT do repositório. | Conferir direitos dos materiais terceiros, XML e imagens. |
| 37 | `Plan_Data_V3.py` | 2,216 | P2 | Data fixture na raiz duplicável com versão na pasta. | Centralizar fixture; manter wrapper histórico. |
| 38 | `Plan_V3_funcional.py` | 11,005 | P2 | Cópia paralela do app funcional do V3. | Escolher canônico após diff/testes. |
| 39 | `Plotly_Guides/About_Guides_XLMextratction.md` | 1 | P2 | Arquivo contém apenas quebra de linha. | Preencher índice e indicar XMLs ou eliminar em PR específico. |
| 40 | `Python_colab_tutorial_Part_1_V001.ipynb` | 119,325 | P2 | 214 células, 1 saída histórica KeyError. | Reter como material didático e marcar execução não garantida. |
| 41 | `python-colab.ipynb` | 165,451 | P2 | 180 células, 2 saídas históricas de erro. | Preservar e adicionar execução limpa opcional em CI. |
| 42 | `README_VISUAL_PROPOSTA.md` | 5,102 | P2 | Arquivo catalogado; verificação detalhada de comportamento pendente. | Preservar, estabelecer testes/evidência e manter vínculo com objetivo. |
| 43 | `README.md` | 17,072 | P1 | README PT/EN amplo com afirmação V1/V2/V3 totalmente funcionais. | Adicionar badges gerados, galeria Pages, matriz de evidências e limitações. |
| 44 | `RELATORIO_MELHORIAS.md` | 8,790 | P2 | Relatório histórico reclama melhorias concluídas. | Referenciar QA e status real dos bloqueadores. |
| 45 | `RELEASE_NOTES.md` | 9,448 | P2 | Release histórica declara três dashboards funcionais. | Adicionar errata não destrutiva e escopo da revisão. |
| 46 | `requirements.txt` | 314 | P1 | Inspecionado: Dash 2.16/Plotly 5.17/Numpy 1.25 fixos. | Atualizar em branch separada, matriz de versões e lock testado. |
| 47 | `run_app.py` | 6,819 | P1 | Inicialização legada, debug habilitado. | Entrypoint único e flag debug só em desenvolvimento. |
| 48 | `start_app.sh` | 840 | P1 | Inspecionado: caminho /workspaces/... embutido. | Calcular pasta pelo próprio script (dirname). |
| 49 | `sunburst_app_simples_funcionando.py` | 14,426 | P0 | Inspecionado: zeros em pais de hierarquia total. | Mesmo núcleo de árvore; não duplicar regras. |
| 50 | `sunburst_cost_explorer_app.py` | 29,795 | P0 | Inspecionado: zeros em nós pais e branchvalues=total, filtro métrica sem efeito. | Reutilizar agregador totalizado e testes; remover filtros sem efeito. |
| 51 | `sunburst_cost_explorer_funcional.py` | 13,133 | P0 | Versão paralela legacy dos vetores Sunburst. | Arquivar após seleção da versão canônica. |
| 52 | `tema1/chart1.py` | 3,531 | P2 | Exemplo isolado de visualização. | Criar índice de exemplos e export HTML testável. |
| 53 | `tema2/chart2.py` | 6,538 | P2 | Exemplo isolado de visualização. | Criar índice de exemplos e export HTML testável. |
| 54 | `test_app.py` | 956 | P1 | Inspecionado: sys.path.append('/workspaces/Py_Vy_000'). | Migrar para pytest importável e caminho relativo. |
| 55 | `test_dash_simple.py` | 508 | P1 | Inspecionado: app.run_server legado. | Atualizar para app.run; transformar em smoke test não bloqueante. |
| 56 | `v006_rvw.ipynb` | 747,164 | P1 | 237 células, 3 saídas históricas de erro (2 SyntaxError; 1 AssertionError). | Preservar original; exportar código reaproveitável/testes. |

## Falhas cross-domain

- **Engenharia de dados**: separar dados sintéticos de valores de obra real. O V1 (53 quantias) e o V2 Python (49 folhas; 3.085.000 custo; 2.988.000 orçamento) são conjuntos distintos. Não combinar sem chave/proveniência.
- **Visualização**: `ids` únicos de caminhos; cada `parent` existente; em `branchvalues='total'` cada nó agregador deve somar filhos. Valores negativos de variância não dimensionam setores.
- **ML**: V3 = 10 observações; coeficientes absolutos de regressão com unidades distintas não definem importância comparável. Exigir holdout/CV, baseline, MAE, métricas honestas antes de chamar preditivo.
- **PMO/Engenharia Civil**: EAP real do Apartamento 91 exige ID da versão, WBS, unidade, etapa, estado orçamentário, fonte, validade da medição e reconciliação; não misturar automaticamente dados sintéticos.
- **Deployment**: GitHub Pages é site estático; Dash requer servidor Python em infraestrutura separada. Build de Pages deve exportar figuras e cálculos durante CI, sem aceitar código/CSV de terceiros durante a publicação sem validação.
- **Segurança/privacidade**: não incluir custos pessoais ou documentos da obra sem filtragem, anonimização e autorização expressa; URLs públicas tornam dados acessíveis a todos.

## Gate recomendado

1. Corrigir integridade hierárquica e reconciliar totais, testar 100% referências pai/filho.
2. Gerar V1/V2/V3 como páginas offline com Plotly embutido e dataset versionado.
3. Validar CLI, lint, testes de valores, HTML e abertura em navegador real.
4. Publicar Pages **apenas após aprovação de PR** na main; branch de auditoria e PR não acionam deploy público.

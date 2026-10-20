# Auditoria e roadmap de publicação — 2026-10-19

> Base imutável da revisão: `main` / `859aa2882b290268d46d7027b4eb437cb844914b`.
> Esta branch de revisão não altera a `main`. Aplique as correções após revisão de PR.

## Inventário Git confirmado

- 53 arquivos e 15 diretórios (árvore recursiva Git).
- 3 notebooks Jupyter, 4 HTMLs estáticos em `index/`, 3 guias XML grandes.
- Aplicações Dash V1/V2/V3 e múltiplas variações históricas no diretório raiz.
- Sem `.github/workflows` na árvore auditada. Este PR propõe um workflow inicial.

## Matriz P0–P3

| ID | Criticidade | Artefatos | Evidência | Correção |
|---|---|---|---|---|
| A01 | P0 | `v006_rvw.ipynb` | 237 células, 87 código, 63 sem execution_count; 3 erros guardados | Extrair pipeline estável, mover texto inválido (1,37,183), remover execução de servidor embutida e validar execução isolada |
| A02 | P0 | `index/*.html` | HTMLs V1–V3 carregam `plotly-latest.min.js` de CDN | Pin de dependência ou bundle Plotly local e geração offline versionada |
| A03 | P0 | `index/` / Pages | Landing é `principal.html`, não `index.html` na raiz de publicação | Gerar `_site/index.html` a partir da landing e publicar via Actions |
| A04 | P0 | `index/dashboard_v3.html` | Exibe pesos de importância `[0.75, 0.85, 0.15]` explicitamente simulados | Não representar como ML validado; diferenciar demonstração de avaliação reprodutível |
| A05 | P1 | `requirements.txt` | Pins de 2023–24 sem matriz de Python/lock | Testar Python 3.11, conferir versões compatíveis e gerar lock/constraints |
| A06 | P1 | `run_app.py`, `app_simples.py`, `test_dash_simple.py` | `run_server(debug=True)`, servidor no import em `run_app.py` | `app.run` com guard, debug por variável de ambiente, smoke-test |
| A07 | P1 | `start_app.sh` / `test_app.py` | Paths `/workspaces/Py_Vy_000` e `pkill -f` genérico | Paths relativos e encerramento pelo PID conhecido, evitar matar processos alheios |
| A08 | P1 | `Plan_Data_V3.py` (duas cópias) | RNG não determinístico sem seed | Fixtures CSV versionadas, dados sintéticos explicitamente marcados |
| A09 | P1 | `index/dashboard_v2.html` vs `v006_rvw.ipynb` | Base V2: 23 itens, US$4.730.000; v006 (célula 17): 23 itens, US$3.085.000 | Separar versões e usar checksums e reconciliação por fonte |
| A10 | P1 | `docs/API_REFERENCE.md` | API documentada inclui nomes de funções não localizados nas implementações inspecionadas | Verificar símbolos públicos e gerar referência a partir de código |
| A11 | P1 | `dashboards/v2_construction/V2_script.py` | `app.run(debug=True,jupyter_mode='inline')` incompatível com execução CLI padronizada | Separar modo notebook e CLI com porta documentada |
| A12 | P1 | `docs/technical_documentation.md` | Instruções de deploy para servidor Python e documentação de portas desacopladas de Pages | Especificar deploy estático (sem Dash) e host servidor separado |
| A13 | P2 | `python-colab.ipynb` | 88 células de código sem execution_count e erros históricos KeyError/TypeError | Ensaio controlado com nbclient, correções por célula |
| A14 | P2 | `Python_colab_tutorial_Part_1_V001.ipynb` | 214 células; erro histórico KeyError monkey | Testes sem efeitos laterais e organização de capítulos |
| A15 | P2 | `docs/*guide.xml` | Fontes XML grandes, alto custo de manutenção; sem testes de estrutura | Validar XML, separar índice e extrair catálogos |
| A16 | P2 | `README.md`, `COMO_EXECUTAR.md` | Documentação heterogênea, caminhos locais fixos | Leia-me único com demos, comandos replicáveis e disclaimer |
| A17 | P2 | `error_reports/complete_error_analysis.md` | Erros documentados como histórico, mas sem regressões automáticas | Criar testes de regressão por bug |
| A18 | P3 | `assets/*` | Assets visuais sem manifesto de licença/proveniência em código | Manifesto de fontes/licenças, alt text e otimização |

## Estratégia de publicação

O workflow `.github/workflows/pages.yml` valida as quatro páginas existentes, constrói
`_site/index.html` copiando `index/principal.html` e publica somente em push para `main`.
Um PR executa apenas a validação/preview, não o deploy. Após aprovação, selecionar
**Settings > Pages > Build and deployment > Source: GitHub Actions**. Bloquear o
ambiente `github-pages` para deploy de `main`.

**Importante:** nesta etapa o workflow publica os HTMLs já existentes; estes ainda dependem de CDN.
Para suporte offline, substituir o build por exportação Plotly com `include_plotlyjs=True`,
usar arquivos de dados versionados e testes de renderização headless.

## Critérios de aceite da revisão

1. `main` sem commits não aprovados; PR draft e diffs revisados.
2. Entradas `index.html`, V1, V2, V3 acessíveis na mesma base URL após deploy.
3. Total V2 = 4.730.000 USD e orçamento = 4.557.000 USD em fixture isolada.
4. V3 rotulado como dataset sintético e sem promessas de desempenho de ML não validadas.
5. Teste HTML offline não deve requisitar scripts externos.
6. Dash CLI e Jupyter passam em CI sob versão Python suportada.
7. Core Web Vitals, teclado, contraste e mobile revisados por captura real no navegador.

## Plano de implementação

- **R0 (feito nesta branch):** esqueleto Pages/CI, README visual e auditoria.
- **R1:** estabilizar dados, dependências e scripts; corrigir notebook V006.
- **R2:** gerar HTML offline a partir do pipeline, parar de editar datasets em duas linguagens.
- **R3:** testes estáticos, smoke Dash, acessibilidade, renderização, performance.
- **R4:** deploy Pages condicionado à aprovação do PR e proteção do ambiente.

Não confundir estrutura auditada com execução completa: os notebooks Colab e os apps Dash
não foram executados integralmente nesta auditoria. Os guias XML e imagens foram
inventariados; para validação semântica de todas as entradas/imagens é necessário um
processamento complementar específico.

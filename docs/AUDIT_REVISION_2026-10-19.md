# Auditoria técnica cruzada — 2026-10-19

**Escopo:** Python-Data-Driven-Visualization-Journey. Baseline `main@859aa2882b290268d46d7027b4eb437cb844914b`. Revisão: `audit/pages-selfcontained-20261019`. Os 53 blobs da árvore estão rastreados individualmente em [FILE_INVENTORY_2026-10-19.md](FILE_INVENTORY_2026-10-19.md).

## Limitação metodológica
Esta é uma inspeção estática de repositório, metadados, código e arquivos de texto; não é atestado de execução ponta a ponta. Notebook e XML grandes receberam inventário e amostragem; não foram integralmente reexecutados/validados. Arquivos de imagem foram inventariados; não houve avaliação perceptual de cada asset. A correção funcional dos aplicativos Dash originais depende de CI e de execução controlada. Há uma camada nova HTML offline, **não** equivalência funcional completa ao Dash.

## Matriz de achados confirmados e propostas

| ID | P | Evidência | Efeito | Proposta | Teste de aceite |
|---|---|---|---|---|---|
| DATA-01 | P0 | V1 Python: 97 labels, 97 parents, **53 values** | Hierarquia desalinhada | IDs únicos, vetores iguais, relações pai verificadas, soma apenas de folhas | Assert estrutural e teste sunburst |
| DATA-02 | P0 | V2 HTML: 23 registros = **US$ 4.730.000** realizados, **US$ 4.557.000** orçados; KPI inicial aponta US$ 2,5M | Inconsistência visual/numérica | Indicadores calculados de um único dataset | Desvio exatamente **US$ 173.000** |
| DATA-03 | P1 | Duas cópias de Plan_Data_V3.py com SHA igual | Drift e duplicação | Fonte única, seed fixa, versionamento de dados | Determinismo em reexecução |
| MODEL-01 | P0 | `Plan_V3.py`: df_complex não definido no módulo | Potencial NameError | Import/carga explícita | Smoke de import isolado |
| MODEL-02 | P0 | V3 HTML mostra importâncias [0.75,0.85,0.15] estáticas | Inferência enganosa de ML | Remover métricas fictícias e publicar MAE/RMSE apenas com avaliação fora da amostra | Baseline e proveniência documentados |
| DEPLOY-01 | P0 | HTML legado V1/V2/V3 usa `plotly-latest.min.js` via CDN | Não funciona offline | Novo `site/` sem dependência remota | Browser com rede bloqueada |
| DEPLOY-02 | P1 | HTML está em `index/`, sem index.html na raiz | Falha possível de URL principal | Publicar `site/` por Actions | URL Pages abre landing |
| DEV-01 | P1 | `start_app.sh`: shebang depois de echo, `pkill -f python.*app` e venv absoluto | Processos encerrados indevidamente e ambiente não portátil | Venv relativo, trap/PID único, shellcheck | Execução isolada e idempotente |
| DEV-02 | P1 | Dash inicializa em 0.0.0.0 com debug ligado em múltiplos pontos | Exposição involuntária | Bind 127.0.0.1 por padrão; opt-in explícito | Smoke em modo seguro |
| DEPLOY-03 | P1 | `docs/technical_documentation.md` aponta Gunicorn para objeto Dash :app | WSGI potencialmente incorreto | Usar `server=app.server` e apontar :server | HTTP 200 |
| DOC-01 | P1 | README e Release Notes descrevem 3 apps como plenamente concluídos | Maturidade não sustentada por CI reproduzível | README visual com status de cada etapa | Status apoiado em checks |
| DEP-01 | P1 | Requirements pins 2023–24 em Python de referência 3.12 | Compatibilidade sem validação recente | Revisão de dependências com matriz Python/OS | Pip install, compileall, smoke |
| A11Y-01 | P2 | Verificação de contraste/teclado ausente | Dificuldade de acessibilidade | WCAG 2.2 AA, navegação teclado, label e estado vazio | axe-core + testes manuais |

## Mudanças implementadas nesta branch

- `site/index.html`, `site/dashboard_v1.html`, `site/dashboard_v2.html`, `site/dashboard_v3.html`: quatro artefatos HTML completos, CSS+JavaScript+dados inline, sem CDN. V1 é **reconstrução didática sobre dados V2**, pois a origem V1 requer correção. V2 usa 23 dados ilustrativos e V3 usa 10 exemplos sintéticos; não executam Dash nem ML real.
- `.github/workflows/pages.yml`: deploy restrito à `main`, de modo que a revisão não publica automaticamente.
- `README_REDESIGN_PROPOSAL.md`: proposta visual **não substitui** o README da main nesta etapa.
- `docs/FILE_INVENTORY_2026-10-19.md`: 53 arquivos rastreados, com status, classe e ação.

## Plano em fases e gates

1. **Gate G0 — Segurança e rastreabilidade:** branch protegida; baixar baseline; adicionar lint, pipeline, matrizes de datasets e teste de dependências.
2. **Gate G1 — Dados:** corrigir vetores V1, identificar folhas, agregações, ids; remover dados duplicados e métricas hardcoded.
3. **Gate G2 — Frontend:** testar site offline em Chromium/Firefox, 320px–1920px, filtros em cascata, seleção vazia, exportação e acessibilidade.
4. **Gate G3 — Python:** `pytest` cobrindo callbacks, import, datasets; separar app demo e script de teste; tornar debug seguro.
5. **Gate G4 — ML:** com dados observacionais reais suficientes, separação temporal/holdout, baselines, MAE/RMSE, análise de leakage, validação de explicabilidade. Enquanto isso, rotular as visualizações como **ilustrativas**.
6. **Gate G5 — Pages:** revisão PR, merge opcional, `Settings → Pages → Build and deployment → GitHub Actions`, acompanhar Actions e testar URL pública.
7. **Gate G6 — README:** substituir README apenas depois de screenshots e URLs implantadas estarem verificadas; badges devem refletir resultados, não promessas.

## Arquitetura-alvo

```text
data/  →  contracts/  →  apps/dash/{v1,v2,v3}
             └──────────→ static-build/ (JSON offline) → site/
tests/ ──────────────────→ pull_request CI
main push ───────────────→ pages.yml → GitHub Pages
```

**Trade-off:** Pages é estático. Para callbacks Python/ML de verdade em produção, usar um backend separado (Render/Fly.io/Cloud Run ou equivalente), com custos, autenticação e segurança próprios. Não mascarar simulação como predição.

## Links externos de fundamentação
- [GitHub Pages com Actions](https://docs.github.com/pt/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub Pages workflows](https://docs.github.com/pt/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Plotly Python write_html](https://plotly.com/python-api-reference/generated/plotly.io.html)

# Roadmap técnico · auditoria federada (19/10/2026)

> Base: `main` SHA `20486531a623c48e99bf6e529e13c28155b56603`. **Nenhum merge automático.**

## Escopo medido
- 62 arquivos Git no Journey (80 entradas incluindo diretórios).
- 763 arquivos no Predictive Dashboard; 264 no Handbook; 415 no monitor eleitoral (repo externo somente leitura).
- Total: 1.504 arquivos sob **triagem estrutural**. Isso NÃO equivale a leitura/execução integral do conteúdo de cada arquivo.
- Inventário: `docs/audit/FILE_INVENTORY_MULTI_REPO.csv`. Problemas: `docs/audit/ISSUE_MATRIX.csv` (21 itens, graus de evidência distintos).

## Fases com dependências / gates
| Ordem | Gate | Atividade | Aceite |
|---|---|---|---|
| F0 | SHA e PR #9 reconciliados | Congelar baseline; evitar retrabalho com `audit/offline-pages-2026-10-19` | Diff conhecido |
| F1 | Bloqueante | Corrigir CSV V2 (8 linhas inválidas); garantir parsing com 7 colunas | 49 linhas, valor de custo 3.085.000 |
| F2 | F1 | Exportador reproduzível V1/V2/V3 → HTML autossuficiente | 5 HTMLs que funcionam sem internet |
| F3 | F2 | CI: validate → unittest → build preview → deploy só em main | PR sem publicação |
| F4 | F1 | App factory, paths baseados em __file__, debug off, pytest | Execução local segura |
| F5 | F1/F4 | Review do ML V3: sample n=10, CV/holdout, importância de variáveis | Sem reivindicação preditiva não validada |
| F6 | F2/F3 | README visual, manifest, AGENTS e docs de Pages | Navegação e proveniência |
| F7 | F6 | Federação com Predictive, Handbook e QA elections | Links e licenças preservados |

## Decisões
1. GitHub Pages só executa **HTML/CSS/JavaScript estático**. Dash callbacks requerem processo Python em outro host; nunca prometer live backend no Pages.
2. Página index canônica: `site/index.html`; saídas V1, V2, V3 e auditoria são independentes.
3. HTML verdadeiramente autossuficiente: sem `cdn.plot.ly/plotly-latest.min.js`; usar bundle embutido de Plotly ou gráficos SVG/JS nativos. O protótipo ZIP adota SVG/JS nativos.
4. Fonte de verdade: CSV → gate → export. Não usar números de modelos proxy para descrever o Random Forest do repo Predictive.
5. Handbook contém texto sob licença CC BY-NC-ND de acordo com seu README: referenciar, não fundir o conteúdo.
6. Relatório eleitoral anexado no pedido se mantém isolado como QA; nenhuma projeção será republicada sem verificação.
7. Dependências do Handbook de 2016 ficam em ambiente separado.

## Estado de mudanças no GitHub
- Fix de dados V2 com quoting, commit `b0bd14f` nesta branch.
- Patch Dash da outra aplicação feito **em branch do outro repositório**, também sem alterar sua main.
- Arquivos completos do novo site, geradores, workflow proposto e testes: pacote ZIP gerado para integração no mesmo branch; não declarar hospedagem ativa antes do merge.

## Riscos e objeções
- PR #9 pode conflitar no Pages; rebase/review antes de alterar workflow.
- Uso de pastas `docs/` e `index/` antigas pode ocasionar múltiplos destinos: usar uma fonte única de publicação.
- App Dash com debugger exposto só em rede local de desenvolvimento.
- Dados de exemplo não se tornam reais pelo simples fato de terem passado no validador.
- Teste de navegador/a11y ainda obrigatório, além de testes Python.

## Rollback
Reverter commits da branch ou abandoná-la. Main é preservada. Após merge aprovado, rollback por revert do PR; não usar force push em main.

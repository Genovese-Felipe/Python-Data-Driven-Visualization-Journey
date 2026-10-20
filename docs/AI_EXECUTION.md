# Executabilidade externa e agentes de IA

## Contrato público do portfólio

- Interface estática: `index.html` — dados embutidos, abre offline no navegador.
- Contrato V2: `data/construction_v2.json` — 49 linhas de serviços.
- Contrato V3: `data/smart_home_v3.json` — 10 instalações ilustrativas.
- Manifesto: `data/manifest.json` — proveniência, totais, versão e limitações.
- As rotas publicadas pelo Pages são relativas à base do projeto, não à raiz do domínio.
- Cada item contém ID estável. Não há credenciais nem requisições de rede na interface.

## Como um agente externo executa o repositório

1. Faça checkout de um commit ou branch explicitamente selecionado. Não assuma que `main` contém alterações não incorporadas.
2. Inspecione `data/manifest.json`; trate os exemplos como demonstrativos, nunca como observações financeiras verificadas.
3. Leia os dados por JSON; valide número de linhas, IDs únicos, somatórios e unidades.
4. Para algoritmos Python, crie ambiente isolado; instale dependências compatíveis; execute os scripts explicitamente, sem execução automática de notebooks desconhecidos.
5. Os notebooks e scripts históricos permanecem no repositório, mas **não** estão certificados para execução segura ou sem erros. Rode-os em sandbox sem segredos, com acesso mínimo e limites de recursos.
6. Gere relatórios e propostas em uma branch ou fork, com testes; não altere `main` nem solicite segredo em páginas web.

```python
import json
from pathlib import Path
payload = json.loads(Path("data/construction_v2.json").read_text())
items = payload["records"]
assert len(items) == 49
print(sum(r["cost"] for r in items))  # 3085000 (USD demonstrativos)
```

## Execução remota vs. GitHub Pages

GitHub Pages hospeda HTML/CSS/JS estáticos e JSON. Não hospeda servidores Dash nem executa o backend scikit-learn. Para Python interativo: GitHub Actions, Colab, Codespaces, Hugging Face Spaces, Render/Fly/Railway ou Docker externo. Hospede backend separado e configure CORS, autenticação, limites de uso e segredo no servidor. Não exponha tokens de acesso no JavaScript. Não use Pages como proxy de execução remota.

## Etapas para publicar

- Abrir e revisar o PR da branch `audit/pages-consolidation-20261019`.
- Habilitar proteção de `main`: checks obrigatórios, revisão e bloqueio de push direto.
- Reconciliar as fontes e conferir visualmente os gráficos no browser.
- Depois de aprovado e incorporado: `Settings → Pages → Build and deployment → Source: GitHub Actions`.
- Um push aprovado em `main` executa o job `quality` e, se passar, `deploy`.
- URL esperada **após publicação**: https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/ . Não confundir URL esperada com deployment verificado.

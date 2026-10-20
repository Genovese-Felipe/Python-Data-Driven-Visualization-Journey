# FGen Unified Analytics — revisão

Branch `review/unified-analytics-studio-20261019` separada da `main`. A prévia está em [public/index.html](public/index.html) e combina os gráficos e filtros V1/V2 (49 observações), V3 (dez dados simulados), AP91 **agregado** (1525/224/200) e encaminhamento ao projeto preditivo.

- [Inventário preliminar dos 1.083 arquivos](reports/FILE_BY_FILE_MANIFEST.md) — caminho, SHA, bytes e flags, **não auditoria semântica por conteúdo de cada arquivo**.
- [Repositório do motor preditivo](https://github.com/Genovese-Felipe/Python-Data-Plotly-Predictive-Analytics-Dashboard).
- [Handbook (somente referência)](https://github.com/Genovese-Felipe/PythonDataScienceHandbook). Código MIT; texto CC BY-NC-ND.

**Achados P0/P1:** callback `Output('project-table','data')` num `html.Div` do repo preditivo; trocar por `children`. `exporter.py` usa CDN, impedir falsa promessa offline. Filtro vazio restaura todos os registros. Corrigir em PR próprio no repo preditivo. O material AP91 detalhado exige revisão antes de publicar. GitHub Pages não executa Python/Dash callbacks.

**Próxima ação:** incorporar ao branch de revisão o pacote ZIP completo entregue nesta conversa (app offline completo, JSON, test suite, README visual e deploy), revisando gate de privacidade. Depois abrir PR para `main`.

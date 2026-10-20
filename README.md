<div align="center">

# 📊 Data Driven Visualization Journey

### Engenharia de dados, dashboards e storytelling visual, do Python ao navegador

**🇧🇷 Português | 🇺🇸 English · 3 dashboards · HTML 100% offline**

[🌐 Abrir portfólio (após ativar Pages)](https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/) · [🛠️ Relatório da auditoria](docs/AUDIT_2026-10-19.md) · [📋 Matriz por arquivo](docs/AUDIT_MATRIX.csv)

![Python](https://img.shields.io/badge/Python-Dash%2FPlotly-3776AB?style=for-the-badge) ![Standalone](https://img.shields.io/badge/HTML-Offline-29b99a?style=for-the-badge) ![Status](https://img.shields.io/badge/Status-Em%20revisão-f2a84b?style=for-the-badge)

</div>

> **🔎 Transparência metodológica:** a versão HTML desta branch é uma reconstrução independente e auditável. Os dados são demonstrativos: a V1 usa a hierarquia consistente da V2, enquanto a V3 usa dez exemplos simulados, ainda sem ML validado fora da amostra. Não utilizar números demonstrativos como custos reais.

## ✨ Explore os dashboards

| Módulo | Visual | Experimente |
|:---|:---|:---|
| **V1 · Sunburst** | Hierarquia Pilar → Área, proporção por custo | [HTML independente](dashboard_v1.html) |
| **V2 · Engenharia** | Custo × orçamento, filtros hierárquicos, CSV | [HTML independente](dashboard_v2.html) |
| **V3 · Smart Home** | Dispersão, coordenadas e instalações simuladas | [HTML independente](dashboard_v3.html) |

<p align="center">
<img src="assets/screenshots/dashboard_evolution.png" alt="Captura histórica das versões dos dashboards, sujeita a verificação na auditoria" width="820" />
</p>

### 🚀 Comece em segundos

**Modo offline / sem instalação:** baixe e abra `index.html` no navegador. Cada `dashboard_vN.html` é autossuficiente e funciona isoladamente, sem CDN.

**Versões Python originais (legado sob revisão):**

```bash
git clone https://github.com/Genovese-Felipe/Python-Data-Driven-Visualization-Journey.git
cd Python-Data-Driven-Visualization-Journey
python -m venv .venv
# Ative o ambiente virtual conforme seu sistema operacional
pip install -r requirements.txt
```

> Dependências antigas estão em auditoria: `requirements.txt` ainda não deve ser interpretado como ambiente Python 3.12 validado.

<details><summary><b>📁 Estrutura principal</b></summary>

- `dashboards/v1_simple/` — fonte Python da visualização Sunburst original.
- `dashboards/v2_construction/` — custos, orçamento e filtros.
- `dashboards/v3_smart_home/` — análise de instalações e regressão experimental.
- `index/` — páginas estáticas históricas (CDN, dados divergentes).
- `index.html` e `dashboard_v{1,2,3}.html` — novo portfólio autossuficiente da revisão.
- `docs/AUDIT_2026-10-19.md` e `docs/AUDIT_MATRIX.csv` — auditoria e rastreabilidade.
- `assets/` — screenshots e referências gráficas históricas.
- `ai_learning_guides/`, `docs/`, `error_reports/` — material educacional e manutenção.

</details>

<details><summary><b>🧪 Como interpretar a qualidade analítica?</b></summary>

Os HTMLs podem funcionar sem bibliotecas externas, mas **visualização funcional ≠ modelo estatístico validado**. Custos de V2 são ilustrativos. V3 exige documentação do dataset, controle de leakage, validação cruzada, métricas fora da amostra e comparação com baseline.

</details>

<details><summary><b>🌍 How do I run the demos?</b></summary>

Open `index.html` directly in any modern browser; all charts use native SVG. No Python interpreter, CDN, network access, or build step is necessary. V2 data is illustrative and V3 contains ten simulated records. No validated machine-learning forecast is claimed.

</details>

## 🧭 Roteiro da reconstrução

`Inventário → Dados canônicos → Validação de cálculos → Reconstrução HTML → Testes → Revisão → GitHub Pages`

O plano de implementação e a matriz de 53 arquivos estão disponíveis na documentação. Nenhuma alteração desta revisão foi mesclada na `main`.

## 🏗️ Publicação GitHub Pages

Para prévia sem merge, em **Settings → Pages** selecione **Deploy from a branch**, a branch `audit/offline-pages-2026-10-19` e a pasta **/(root)**. O endereço previsto é `https://genovese-felipe.github.io/Python-Data-Driven-Visualization-Journey/`; **não foi validado como publicado**.

## Autor e licença

[Genovese-Felipe](https://github.com/Genovese-Felipe) · [Licença MIT](LICENSE). Verifique separadamente os direitos dos assets de referência antes de republicá-los.

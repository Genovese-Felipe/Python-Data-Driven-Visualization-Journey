# Py_Vy_000 - Python Data Visualization Repository

Este repositório contém exemplos e aplicações de visualização de dados usando Plotly em Python.

## Estrutura do Repositório

### 📁 index/
Contém o arquivo principal de visualizações em HTML:
- `principal.html` - Dashboard principal com exemplos de gráficos interativos

### 📁 tema1/
Visualizações de Análise de Vendas:
- `chart1.py` - Exemplos de gráficos para análise de dados de vendas
  - Gráfico de barras agrupadas
  - Gráfico de linhas para receita
  - Heatmap de vendas por produto e mês

### 📁 tema2/
Visualizações de Análise Financeira:
- `chart2.py` - Exemplos de gráficos para análise de dados financeiros
  - Gráfico de candlestick
  - Dashboard de portfolio
  - Distribuição de retornos

### 📁 Raiz
- `sunburst_cost_explorer_app.py` - Aplicação Dash com gráfico sunburst para análise de custos
- `sunburst_cost_explorer (7).html` - Visualização HTML gerada

## Como Usar

### Pré-requisitos
```bash
pip install plotly pandas numpy dash
```

### Executar Exemplos

Para executar os exemplos de vendas:
```bash
cd tema1
python chart1.py
```

Para executar os exemplos financeiros:
```bash
cd tema2
python chart2.py
```

Para executar a aplicação Dash:
```bash
python sunburst_cost_explorer_app.py
```

### Visualizar HTML
Abra o arquivo `index/principal.html` em seu navegador para ver o dashboard principal.

## Tecnologias Utilizadas

- **Plotly** - Biblioteca principal para criação de gráficos interativos
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Computação numérica
- **Dash** - Framework para aplicações web analíticas

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
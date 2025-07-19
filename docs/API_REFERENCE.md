# 🚀 **API REFERENCE - Referência Técnica**

## **Core Functions**

### **Data Processing**

#### `create_sunburst_data()`
```python
def create_sunburst_data():
    """
    Cria dados hierárquicos para visualização sunburst
    
    Returns:
        list: Lista de dicionários com estrutura parent-child
        
    Example:
        data = create_sunburst_data()
        # [{'ids': 'total', 'labels': 'Total', 'parents': '', 'values': 100}]
    """
```

#### `process_construction_data()`
```python
def process_construction_data():
    """
    Processa dados de construção para filtros em cascata
    
    Returns:
        pandas.DataFrame: DataFrame estruturado por pilar/categoria/item
        
    Columns:
        - pilar: Categoria principal (Infraestrutura, Acabamentos, etc)
        - categoria: Subcategoria específica
        - item: Item individual de custo
        - valor: Valor monetário em R$
    """
```

#### `generate_smart_home_data()`
```python
def generate_smart_home_data():
    """
    Gera dataset de residências inteligentes para análise ML
    
    Returns:
        pandas.DataFrame: Dataset com features para machine learning
        
    Features:
        - area_m2: Área da residência em metros quadrados
        - num_dispositivos: Número de dispositivos IoT
        - consumo_inicial: Consumo energético antes (kWh)
        - economia_percentual: Economia obtida (%)
        - lat/lon: Coordenadas geográficas
    """
```

### **Machine Learning**

#### `train_energy_model(data)`
```python
def train_energy_model(data):
    """
    Treina modelo de regressão linear para predição de economia energética
    
    Args:
        data (pandas.DataFrame): Dataset com features de entrada
        
    Returns:
        sklearn.linear_model.LinearRegression: Modelo treinado
        
    Features Used:
        - area_m2: Área da residência
        - num_dispositivos: Quantidade de dispositivos
        - consumo_inicial: Consumo base
        
    Target:
        - economia_percentual: Percentual de economia
    """
```

#### `get_feature_importance(model, feature_names)`
```python
def get_feature_importance(model, feature_names):
    """
    Calcula importância das features do modelo treinado
    
    Args:
        model: Modelo sklearn treinado
        feature_names (list): Lista com nomes das features
        
    Returns:
        pandas.DataFrame: DataFrame com feature e importância
        
    Columns:
        - feature: Nome da feature
        - importance: Valor de importância (coeficiente absoluto)
    """
```

### **Visualization Components**

#### `create_sunburst_chart(data)`
```python
def create_sunburst_chart(data):
    """
    Cria gráfico sunburst com dados hierárquicos
    
    Args:
        data (list): Lista de dicts com ids, labels, parents, values
        
    Returns:
        plotly.graph_objects.Figure: Figura sunburst configurada
        
    Configuration:
        - hover_template: Personalizado com valores
        - color_scheme: Cores automáticas
        - size: Responsivo ao container
    """
```

#### `create_geo_scatter(data)`
```python
def create_geo_scatter(data):
    """
    Cria mapa de dispersão geográfico com dados de localização
    
    Args:
        data (pandas.DataFrame): DataFrame com lat, lon e métricas
        
    Returns:
        plotly.express.scatter_geo: Mapa configurado
        
    Features:
        - scope: 'usa' para mapa dos Estados Unidos
        - hover_data: Informações detalhadas no hover
        - color: Baseado na economia percentual
        - size: Proporcional ao número de dispositivos
    """
```

#### `create_regression_plot(data, predictions)`
```python
def create_regression_plot(data, predictions):
    """
    Cria gráfico de dispersão com linha de regressão
    
    Args:
        data (pandas.DataFrame): Dados originais
        predictions (numpy.array): Predições do modelo
        
    Returns:
        plotly.express.scatter: Gráfico com linha de tendência
        
    Elements:
        - scatter: Pontos dos dados reais
        - trendline: Linha de regressão ajustada
        - R²: Coeficiente de determinação
    """
```

#### `create_importance_bar(importance_data)`
```python
def create_importance_bar(importance_data):
    """
    Cria gráfico de barras para importância de features
    
    Args:
        importance_data (pandas.DataFrame): Features e seus valores
        
    Returns:
        plotly.express.bar: Gráfico de barras ordenado
        
    Configuration:
        - orientation: Horizontal
        - sorted: Por valor de importância
        - color: Gradiente baseado em valores
    """
```

### **Callback Functions**

#### V1 - Callbacks (Nenhum)
```python
# V1 não possui callbacks - visualização estática
```

#### V2 - Filter Callbacks
```python
@callback(
    [Output('categoria-dropdown', 'options'),
     Output('categoria-dropdown', 'value')],
    [Input('pilar-dropdown', 'value')]
)
def update_categoria_options(selected_pilar):
    """
    Atualiza opções de categoria baseado no pilar selecionado
    
    Args:
        selected_pilar (str): Pilar selecionado no primeiro dropdown
        
    Returns:
        tuple: (options_list, default_value)
        
    Logic:
        - Filtra categorias disponíveis por pilar
        - Retorna primeira categoria como padrão
        - Lida com seleções vazias
    """

@callback(
    Output('sunburst-graph', 'figure'),
    [Input('pilar-dropdown', 'value'),
     Input('categoria-dropdown', 'value'),
     Input('item-dropdown', 'value')]
)
def update_graph(pilar, categoria, item):
    """
    Atualiza gráfico sunburst baseado nos filtros selecionados
    
    Args:
        pilar (str): Filtro de pilar
        categoria (str): Filtro de categoria  
        item (str): Filtro de item
        
    Returns:
        plotly.graph_objects.Figure: Sunburst atualizado
        
    Logic:
        - Aplica filtros em cascata aos dados
        - Reconstrói hierarquia baseada na seleção
        - Mantém estrutura parent-child consistente
    """
```

#### V3 - Master Callback
```python
@callback(
    [Output('sunburst-graph', 'figure'),
     Output('geo-graph', 'figure'),
     Output('regression-graph', 'figure'),
     Output('importance-graph', 'figure')],
    [Input('filter-dropdown', 'value')]
)
def update_all_graphs(selected_filter):
    """
    Callback master que atualiza todos os 4 gráficos simultaneamente
    
    Args:
        selected_filter (str): Valor do filtro principal
        
    Returns:
        tuple: (sunburst_fig, geo_fig, regression_fig, importance_fig)
        
    Process:
        1. Filtra dados baseado na seleção
        2. Retreina modelo ML com dados filtrados
        3. Atualiza todas as 4 visualizações
        4. Mantém sincronização entre gráficos
    """
```

## **Data Structures**

### **V1 - Sunburst Data**
```python
sunburst_data = [
    {
        'ids': 'total',
        'labels': 'Custo Total', 
        'parents': '',
        'values': 100
    },
    {
        'ids': 'categoria_1',
        'labels': 'Infraestrutura',
        'parents': 'total', 
        'values': 40
    }
    # ... mais 92 itens
]
```

### **V2 - Construction DataFrame**
```python
construction_df = pd.DataFrame({
    'pilar': ['Infraestrutura', 'Acabamentos', ...],
    'categoria': ['Fundação', 'Paredes', ...], 
    'item': ['Concreto', 'Tijolo', ...],
    'valor': [15000, 8000, ...]
})
# Shape: (48, 4)
```

### **V3 - Smart Home Dataset**
```python
smart_home_df = pd.DataFrame({
    'residencia': ['Casa 1', 'Casa 2', ...],
    'area_m2': [120, 85, 200, ...],
    'num_dispositivos': [15, 8, 25, ...],
    'consumo_inicial': [450, 320, 600, ...],
    'economia_percentual': [18, 12, 25, ...],
    'lat': [40.7128, 34.0522, ...],
    'lon': [-74.0060, -118.2437, ...]
})
# Shape: (10, 7)
```

## **Configuration Constants**

### **Ports**
```python
V1_PORT = 8052  # Dashboard V1
V2_PORT = 8050  # Dashboard V2  
V3_PORT = 8053  # Dashboard V3
```

### **Color Schemes**
```python
V2_COLOR_MAP = {
    'Infraestrutura': '#FF6B6B',
    'Acabamentos': '#4ECDC4', 
    'Sistemas': '#45B7D1',
    'Paisagismo': '#96CEB4'
}

V3_COLOR_SCALE = 'Viridis'  # Para mapas geográficos
```

### **Layout Constants**
```python
GRAPH_CONFIG = {
    'displayModeBar': False,  # Remove toolbar
    'responsive': True        # Responsivo
}

STYLE_MAIN = {
    'fontFamily': 'Arial, sans-serif',
    'margin': '20px',
    'backgroundColor': '#f8f9fa'
}
```

## **Error Handling**

### **Common Exceptions**
```python
# Port já em uso
try:
    app.run(port=8050)
except OSError as e:
    if "Address already in use" in str(e):
        print("Porta 8050 em uso. Tentando 8051...")
        app.run(port=8051)

# Dados faltantes  
def safe_filter_data(df, column, value):
    """
    Filtra DataFrame com verificação de existência
    
    Args:
        df: DataFrame para filtrar
        column: Coluna para filtrar
        value: Valor para buscar
        
    Returns:
        DataFrame: Dados filtrados ou original se erro
    """
    try:
        if value in df[column].unique():
            return df[df[column] == value]
        else:
            return df
    except KeyError:
        print(f"Coluna {column} não encontrada")
        return df

# Callback errors
@callback(...)
def safe_callback(*args):
    """
    Callback com tratamento de erro
    """
    try:
        # Lógica principal
        return generate_figure()
    except Exception as e:
        print(f"Erro no callback: {e}")
        return empty_figure()
```

---

## **Performance Tips**

### **Otimização de Dados**
```python
# ❌ Evitar - processamento a cada callback
@callback(...)
def slow_callback():
    df = pd.read_csv('large_file.csv')  # Lento!
    return process_data(df)

# ✅ Melhor - cache global
DATA_CACHE = pd.read_csv('large_file.csv')

@callback(...)
def fast_callback():
    return process_data(DATA_CACHE)  # Rápido!
```

### **Callback Optimization**
```python
# ❌ Evitar - múltiplos callbacks
@callback(Output('graph1', 'figure'), Input('dropdown', 'value'))
def update_graph1(): pass

@callback(Output('graph2', 'figure'), Input('dropdown', 'value'))  
def update_graph2(): pass

# ✅ Melhor - callback único com múltiplas saídas
@callback(
    [Output('graph1', 'figure'), Output('graph2', 'figure')],
    Input('dropdown', 'value')
)
def update_both_graphs():
    return fig1, fig2
```

---

*Esta API reference cobre todas as funções principais dos 3 dashboards. Para detalhes de implementação, consulte o código fonte.*

#!/usr/bin/env python3
"""A simplified Dash dashboard for exploring construction costs.

This script creates a basic, standalone Dash application that visualizes
a small, hardcoded dataset of construction costs. It is intended as a
simple example or a starting point for more complex dashboards.

The dashboard features:
- Summary cards for total cost, total budget, and total variance.
- A dropdown filter to select a project category.
- A bar chart that compares the actual value vs. the budget.
- A sunburst chart that shows the hierarchical distribution of costs.
"""
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Load data from the CSV file.
df = pd.read_csv('data/app_simples_data.csv')

# Criar aplicativo
app = Dash(__name__)
# The main Dash application instance for the simple app.

app.layout = html.Div([
    # The main container for the simple app's layout.
    # Main title of the dashboard.
    html.H1("🏗️ Explorador de Custos de Construção", 
            style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}),
    
    # Container for the summary metric cards.
    html.Div([
        # Card displaying the total cost.
        html.Div([
            html.H3(f"${df['valor'].sum():,.0f}", style={'color': '#3498db', 'margin': '0'}),
            html.P("Custo Total", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
        ], style={'textAlign': 'center', 'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '8px', 'width': '200px', 'margin': '10px'}),
        
        # Card displaying the total budget.
        html.Div([
            html.H3(f"${df['orcamento'].sum():,.0f}", style={'color': '#95a5a6', 'margin': '0'}),
            html.P("Orçamento Total", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
        ], style={'textAlign': 'center', 'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '8px', 'width': '200px', 'margin': '10px'}),
        
        # Card displaying the total variance.
        html.Div([
            html.H3(f"${df['valor'].sum() - df['orcamento'].sum():,.0f}", style={'color': '#e74c3c', 'margin': '0'}),
            html.P("Variação", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
        ], style={'textAlign': 'center', 'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '8px', 'width': '200px', 'margin': '10px'}),
    ], style={'display': 'flex', 'justifyContent': 'center', 'marginBottom': '30px'}),
    
    # Dropdown to filter data by category.
    dcc.Dropdown(
        id='categoria-dropdown',
        options=[{'label': 'Todas', 'value': 'todas'}] + 
                [{'label': cat, 'value': cat} for cat in df['categoria'].unique()],
        value='todas',
        style={'marginBottom': '20px', 'width': '300px', 'margin': '0 auto'}
    ),
    
    # Placeholder for the bar chart visualization.
    dcc.Graph(id='grafico-barras'),
    # Placeholder for the sunburst chart visualization.
    dcc.Graph(id='grafico-sunburst'),
    
    # A simple status message at the bottom of the app.
    html.Div([
        html.P("✅ Aplicativo funcionando corretamente!", 
               style={'textAlign': 'center', 'color': '#27ae60', 'fontSize': '18px', 'fontWeight': 'bold'}),
        html.P("Acesse: http://localhost:8050", 
               style={'textAlign': 'center', 'color': '#3498db', 'fontSize': '16px'})
    ], style={'marginTop': '30px', 'padding': '20px', 'backgroundColor': '#e8f6f3', 'borderRadius': '8px'})
])

@app.callback(
    [Output('grafico-barras', 'figure'),
     Output('grafico-sunburst', 'figure')],
    [Input('categoria-dropdown', 'value')]
)
def atualizar_graficos(categoria_selecionada):
    """Updates the bar and sunburst charts based on the selected category.

    This callback function filters the DataFrame based on the value from the
    category dropdown. It then generates a new bar chart comparing actual
    value vs. budget and a sunburst chart showing the hierarchical cost
    distribution for the selected category.

    Args:
        categoria_selecionada (str): The category selected from the dropdown.

    Returns:
        tuple: A tuple containing two Plotly Figure objects:
            - fig_bar: The updated bar chart.
            - fig_sunburst: The updated sunburst chart.
    """
    if categoria_selecionada == 'todas':
        df_filtrado = df
    else:
        df_filtrado = df[df['categoria'] == categoria_selecionada]
    
    # Gráfico de barras
    fig_bar = px.bar(
        df_filtrado, 
        x='subcategoria', 
        y=['valor', 'orcamento'],
        title='Comparação: Valor Real vs Orçamento',
        color_discrete_map={'valor': '#3498db', 'orcamento': '#95a5a6'}
    )
    fig_bar.update_layout(
        xaxis_title='Subcategoria',
        yaxis_title='Valor ($)',
        font={'family': 'Arial, sans-serif'},
        height=400
    )
    
    # Sunburst
    fig_sunburst = px.sunburst(
        df_filtrado,
        path=[px.Constant("Total"), 'categoria', 'subcategoria'],
        values='valor',
        title='Distribuição Hierárquica de Custos'
    )
    fig_sunburst.update_layout(
        font={'family': 'Arial, sans-serif'},
        height=500
    )
    
    return fig_bar, fig_sunburst

if __name__ == '__main__':
    print("🚀 Iniciando aplicativo Dash...")
    print("📊 Servidor rodando em: http://localhost:8050")
    print("🔄 Pressione Ctrl+C para parar")
    app.run_server(debug=True, port=8050, host='0.0.0.0')

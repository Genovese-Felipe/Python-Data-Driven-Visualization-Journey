#!/usr/bin/env python3

from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Dados simplificados para teste
data_simples = [
    {'categoria': 'Design', 'subcategoria': 'Arquitetura', 'valor': 100000, 'orcamento': 95000},
    {'categoria': 'Design', 'subcategoria': 'Engenharia', 'valor': 150000, 'orcamento': 145000},
    {'categoria': 'Construção', 'subcategoria': 'Fundação', 'valor': 300000, 'orcamento': 290000},
    {'categoria': 'Construção', 'subcategoria': 'Estrutura', 'valor': 500000, 'orcamento': 510000},
]

df = pd.DataFrame(data_simples)

# Criar aplicativo
app = Dash(__name__)

app.layout = html.Div([
    html.H1("🏗️ Explorador de Custos de Construção", 
            style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}),
    
    html.Div([
        html.Div([
            html.H3(f"${df['valor'].sum():,.0f}", style={'color': '#3498db', 'margin': '0'}),
            html.P("Custo Total", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
        ], style={'textAlign': 'center', 'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '8px', 'width': '200px', 'margin': '10px'}),
        
        html.Div([
            html.H3(f"${df['orcamento'].sum():,.0f}", style={'color': '#95a5a6', 'margin': '0'}),
            html.P("Orçamento Total", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
        ], style={'textAlign': 'center', 'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '8px', 'width': '200px', 'margin': '10px'}),
        
        html.Div([
            html.H3(f"${df['valor'].sum() - df['orcamento'].sum():,.0f}", style={'color': '#e74c3c', 'margin': '0'}),
            html.P("Variação", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
        ], style={'textAlign': 'center', 'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '8px', 'width': '200px', 'margin': '10px'}),
    ], style={'display': 'flex', 'justifyContent': 'center', 'marginBottom': '30px'}),
    
    dcc.Dropdown(
        id='categoria-dropdown',
        options=[{'label': 'Todas', 'value': 'todas'}] + 
                [{'label': cat, 'value': cat} for cat in df['categoria'].unique()],
        value='todas',
        style={'marginBottom': '20px', 'width': '300px', 'margin': '0 auto'}
    ),
    
    dcc.Graph(id='grafico-barras'),
    dcc.Graph(id='grafico-sunburst'),
    
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

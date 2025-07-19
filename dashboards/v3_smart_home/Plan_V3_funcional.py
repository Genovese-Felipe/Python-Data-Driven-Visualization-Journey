#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plan V3 - Smart Home Installation Analytics Dashboard
Versão corrigida e funcional
"""

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

# ===== DADOS SIMULADOS =====
# Baseados no Plan_Data_V3.py mas integrados no próprio arquivo

data = {
    'Region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East', 'West', 'West'],
    'City': ['Seattle', 'Seattle', 'Portland', 'Austin', 'Dallas', 'Houston', 'New York', 'Boston', 'San Francisco', 'Los Angeles'],
    'Installation_Type': ['Solar Panels', 'Smart Thermostat', 'Solar Panels', 'Smart Thermostat', 'Security System', 'Solar Panels', 'Smart Thermostat', 'Security System', 'Solar Panels', 'Smart Thermostat'],
    'Installation_Cost': [15000, 8000, 18000, 6000, 12000, 20000, 7500, 14000, 22000, 9000],
    'Annual_Energy_Savings': [1800, 900, 2100, 750, 800, 2400, 850, 900, 2600, 950],
    'Number_of_Devices': [8, 5, 10, 4, 12, 9, 6, 11, 12, 7],
    'Customer_Satisfaction': [4.2, 3.8, 4.5, 4.0, 4.3, 4.1, 3.9, 4.4, 4.6, 4.2],
    'Latitude': [47.6062, 47.6062, 45.5051, 30.2672, 32.7767, 29.7604, 40.7128, 42.3601, 37.7749, 34.0522],
    'Longitude': [-122.3321, -122.3321, -122.6750, -97.7431, -96.7970, -95.3698, -74.0060, -71.0589, -122.4194, -118.2437]
}

df_complex = pd.DataFrame(data)

# ===== ANÁLISE PREDITIVA =====
# Preparar dados para predição de economia de energia
X = df_complex[['Installation_Cost', 'Number_of_Devices', 'Customer_Satisfaction']]
y = df_complex['Annual_Energy_Savings']

# Treinar modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# Importância das features (coeficientes absolutos)
feature_importance = pd.DataFrame({
    'feature': ['Installation Cost', 'Number of Devices', 'Customer Satisfaction'],
    'importance': np.abs(model.coef_)
}).sort_values('importance', ascending=False)

# ===== APLICAÇÃO DASH =====
app = Dash(__name__)
app.title = "🏡 Smart Home Analytics Dashboard"

# Layout do Dashboard
app.layout = html.Div([
    # Cabeçalho
    html.Div([
        html.H1("🏡 Smart Home Installation Analytics Dashboard", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}),
        
        html.P("Análise abrangente de instalações de casa inteligente com visualizações complexas e análise preditiva", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '18px'})
    ], style={'marginBottom': '30px'}),
    
    # Filtros
    html.Div([
        html.Div([
            html.Label("Região:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            dcc.Dropdown(
                id='region-dropdown',
                options=[{'label': i, 'value': i} for i in df_complex['Region'].unique()] + [{'label': 'Todas', 'value': 'All'}],
                value='All',
                clearable=False,
                style={'marginBottom': '15px'}
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'marginRight': '3%'}),

        html.Div([
            html.Label("Cidade:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            dcc.Dropdown(
                id='city-dropdown',
                options=[{'label': i, 'value': i} for i in df_complex['City'].unique()] + [{'label': 'Todas', 'value': 'All'}],
                value='All',
                clearable=False,
                style={'marginBottom': '15px'}
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'marginRight': '3%'}),

        html.Div([
            html.Label("Tipo de Instalação:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            dcc.Dropdown(
                id='type-dropdown',
                options=[{'label': i, 'value': i} for i in df_complex['Installation_Type'].unique()] + [{'label': 'Todos', 'value': 'All'}],
                value='All',
                clearable=False,
                style={'marginBottom': '15px'}
            ),
        ], style={'width': '30%', 'display': 'inline-block'}),
    ], style={
        'padding': '20px', 
        'backgroundColor': '#f8f9fa', 
        'borderRadius': '10px',
        'marginBottom': '30px'
    }),

    # Linha superior de gráficos
    html.Div([
        # Sunburst hierárquico
        html.Div([
            html.H3("📊 Distribuição Hierárquica", style={'textAlign': 'center', 'color': '#2c3e50'}),
            dcc.Graph(id='hierarchical-chart')
        ], style={
            'width': '48%', 
            'display': 'inline-block', 
            'marginRight': '4%',
            'backgroundColor': 'white',
            'padding': '15px',
            'borderRadius': '10px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
        }),

        # Mapa geográfico
        html.Div([
            html.H3("🗺️ Distribuição Geográfica", style={'textAlign': 'center', 'color': '#2c3e50'}),
            dcc.Graph(id='map-visualization')
        ], style={
            'width': '48%', 
            'display': 'inline-block',
            'backgroundColor': 'white',
            'padding': '15px',
            'borderRadius': '10px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
        }),
    ], style={'marginBottom': '30px'}),

    # Linha inferior de gráficos
    html.Div([
        # Scatter plot
        html.Div([
            html.H3("💰 Custo vs. Economia", style={'textAlign': 'center', 'color': '#2c3e50'}),
            dcc.Graph(id='scatter-plot')
        ], style={
            'width': '48%', 
            'display': 'inline-block', 
            'marginRight': '4%',
            'backgroundColor': 'white',
            'padding': '15px',
            'borderRadius': '10px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
        }),

        # Análise preditiva
        html.Div([
            html.H3("🔮 Importância dos Fatores", style={'textAlign': 'center', 'color': '#2c3e50'}),
            dcc.Graph(id='predictive-viz')
        ], style={
            'width': '48%', 
            'display': 'inline-block',
            'backgroundColor': 'white',
            'padding': '15px',
            'borderRadius': '10px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
        }),
    ])
], style={
    'padding': '20px',
    'fontFamily': 'Arial, sans-serif',
    'backgroundColor': '#ecf0f1'
})

# ===== CALLBACKS =====

# Callback para atualizar opções de cidade baseado na região
@app.callback(
    Output('city-dropdown', 'options'),
    Output('city-dropdown', 'value'),
    Input('region-dropdown', 'value')
)
def update_cities(selected_region):
    if selected_region == 'All':
        cities = df_complex['City'].unique()
    else:
        cities = df_complex[df_complex['Region'] == selected_region]['City'].unique()
    
    city_options = [{'label': i, 'value': i} for i in cities] + [{'label': 'Todas', 'value': 'All'}]
    return city_options, 'All'

# Callback principal para atualizar todos os gráficos
@app.callback(
    Output('hierarchical-chart', 'figure'),
    Output('map-visualization', 'figure'),
    Output('scatter-plot', 'figure'),
    Output('predictive-viz', 'figure'),
    Input('region-dropdown', 'value'),
    Input('city-dropdown', 'value'),
    Input('type-dropdown', 'value')
)
def update_dashboard(selected_region, selected_city, selected_type):
    # Filtrar dados
    filtered_df = df_complex.copy()
    
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    if selected_city != 'All':
        filtered_df = filtered_df[filtered_df['City'] == selected_city]
    if selected_type != 'All':
        filtered_df = filtered_df[filtered_df['Installation_Type'] == selected_type]

    # ===== GRÁFICO SUNBURST HIERÁRQUICO =====
    if not filtered_df.empty:
        hierarchical_fig = px.sunburst(
            filtered_df,
            path=['Region', 'City', 'Installation_Type'],
            values='Installation_Cost',
            color='Installation_Cost',
            color_continuous_scale='Viridis',
            title='Distribuição de Custos por Região > Cidade > Tipo'
        )
        hierarchical_fig.update_traces(
            hovertemplate='<b>%{label}</b><br>Custo: $%{value:,.0f}<br>Percentual: %{percentParent}<extra></extra>'
        )
    else:
        hierarchical_fig = go.Figure()
        hierarchical_fig.add_annotation(text="Nenhum dado disponível", showarrow=False)
    
    hierarchical_fig.update_layout(height=400, margin=dict(t=40, b=0, l=0, r=0))

    # ===== MAPA GEOGRÁFICO =====
    if not filtered_df.empty:
        map_fig = px.scatter_geo(
            filtered_df,
            lat='Latitude',
            lon='Longitude',
            hover_name='City',
            size='Installation_Cost',
            color='Region',
            projection="albers usa",
            title='Instalações nos Estados Unidos'
        )
        map_fig.update_layout(geo=dict(scope='usa'))
        map_fig.update_traces(
            hovertemplate='<b>%{hovertext}</b><br>Custo: $%{marker.size:,.0f}<br>Região: %{marker.color}<extra></extra>'
        )
    else:
        map_fig = go.Figure()
        map_fig.add_annotation(text="Nenhum dado disponível", showarrow=False)
    
    map_fig.update_layout(height=400, margin=dict(t=40, b=0, l=0, r=0))

    # ===== SCATTER PLOT =====
    if not filtered_df.empty:
        scatter_fig = px.scatter(
            filtered_df,
            x='Installation_Cost',
            y='Annual_Energy_Savings',
            color='Installation_Type',
            size='Customer_Satisfaction',
            hover_name='City',
            title='Relação Custo de Instalação vs. Economia Anual'
        )
        scatter_fig.update_traces(
            hovertemplate='<b>%{hovertext}</b><br>Custo: $%{x:,.0f}<br>Economia: $%{y:,.0f}<br>Satisfação: %{marker.size}<extra></extra>'
        )
    else:
        scatter_fig = go.Figure()
        scatter_fig.add_annotation(text="Nenhum dado disponível", showarrow=False)
    
    scatter_fig.update_layout(height=400, margin=dict(t=40, b=20, l=50, r=20))

    # ===== ANÁLISE PREDITIVA =====
    predictive_fig = px.bar(
        feature_importance,
        x='importance',
        y='feature',
        orientation='h',
        color='importance',
        color_continuous_scale='Blues',
        title='Fatores que Mais Influenciam a Economia de Energia'
    )
    predictive_fig.update_layout(
        height=400, 
        margin=dict(t=40, b=20, l=120, r=20),
        yaxis={'categoryorder': 'total ascending'}
    )
    predictive_fig.update_traces(
        hovertemplate='<b>%{y}</b><br>Importância: %{x:.2f}<extra></extra>'
    )

    return hierarchical_fig, map_fig, scatter_fig, predictive_fig

# ===== EXECUÇÃO =====
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8053)

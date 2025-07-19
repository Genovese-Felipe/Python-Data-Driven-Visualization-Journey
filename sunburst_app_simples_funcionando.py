# Sunburst Cost Explorer - VERSÃO SIMPLES E FUNCIONAL
# Criada para garantir que TUDO funcione perfeitamente

from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ===== DADOS =====
data = [
    {'pillar': 'Construction', 'area': 'Superstructure', 'service': 'Framing & Steel', 'task': 'Wood & Steel Frame Erection', 'sub_task': 'Wood Framing', 'cost': 280000, 'budgeted_cost': 275000},
    {'pillar': 'Construction', 'area': 'Superstructure', 'service': 'Framing & Steel', 'task': 'Wood & Steel Frame Erection', 'sub_task': 'Steel Erection', 'cost': 200000, 'budgeted_cost': 198000},
    {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Electrical', 'task': 'Complete Wiring & Fixtures', 'sub_task': 'Wiring Installation', 'cost': 150000, 'budgeted_cost': 145000},
    {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Electrical', 'task': 'Complete Wiring & Fixtures', 'sub_task': 'Fixture Installation', 'cost': 90000, 'budgeted_cost': 88000},
    {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Plumbing & HVAC', 'task': 'Piping, Drains & Ductwork', 'sub_task': 'Plumbing Installation', 'cost': 130000, 'budgeted_cost': 128000},
    {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Plumbing & HVAC', 'task': 'Piping, Drains & Ductwork', 'sub_task': 'HVAC Installation', 'cost': 130000, 'budgeted_cost': 125000},
    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Drywall & Painting', 'task': 'Interior Walls and Ceilings', 'sub_task': 'Drywall Installation', 'cost': 100000, 'budgeted_cost': 98000},
    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Drywall & Painting', 'task': 'Interior Walls and Ceilings', 'sub_task': 'Painting', 'cost': 90000, 'budgeted_cost': 88000},
    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Flooring & Tiling', 'task': 'Hardwood and Ceramic Installation', 'sub_task': 'Hardwood Installation', 'cost': 100000, 'budgeted_cost': 95000},
    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Flooring & Tiling', 'task': 'Hardwood and Ceramic Installation', 'sub_task': 'Tiling', 'cost': 75000, 'budgeted_cost': 73000},
    {'pillar': 'Construction', 'area': 'Superstructure', 'service': 'Roofing', 'task': 'Shingle and Underlayment Installation', 'sub_task': 'Underlayment', 'cost': 40000, 'budgeted_cost': 38000},
    {'pillar': 'Construction', 'area': 'Superstructure', 'service': 'Roofing', 'task': 'Shingle and Underlayment Installation', 'sub_task': 'Shingle Installation', 'cost': 80000, 'budgeted_cost': 78000},
    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Window & Door Installation', 'task': 'Exterior and Interior Openings', 'sub_task': 'Window Installation', 'cost': 50000, 'budgeted_cost': 48000},
    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Window & Door Installation', 'task': 'Exterior and Interior Openings', 'sub_task': 'Door Installation', 'cost': 40000, 'budgeted_cost': 38000},
    # Segundo Pilar
    {'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Cabinetry & Countertops', 'task': 'Kitchen and Bathroom Fixtures', 'sub_task': 'Cabinetry Installation', 'cost': 90000, 'budgeted_cost': 88000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Cabinetry & Countertops', 'task': 'Kitchen and Bathroom Fixtures', 'sub_task': 'Countertop Installation', 'cost': 60000, 'budgeted_cost': 58000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Fixtures & Hardware', 'task': 'Lighting, Faucets, and Door Knobs', 'sub_task': 'Lighting Fixtures', 'cost': 35000, 'budgeted_cost': 34000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Fixtures & Hardware', 'task': 'Lighting, Faucets, and Door Knobs', 'sub_task': 'Faucets and Hardware', 'cost': 35000, 'budgeted_cost': 33000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Hardscaping', 'task': 'Patio, Walkways, and Retaining Walls', 'sub_task': 'Patio and Walkway Construction', 'cost': 50000, 'budgeted_cost': 48000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Hardscaping', 'task': 'Patio, Walkways, and Retaining Walls', 'sub_task': 'Retaining Wall Construction', 'cost': 30000, 'budgeted_cost': 29000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Softscaping', 'task': 'Lawn, Plants, and Trees', 'sub_task': 'Lawn Installation', 'cost': 20000, 'budgeted_cost': 19000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Softscaping', 'task': 'Lawn, Plants, and Trees', 'sub_task': 'Planting and Tree Installation', 'cost': 20000, 'budgeted_cost': 18000}
]

df = pd.DataFrame(data)
df['variance'] = df['cost'] - df['budgeted_cost']
df['variance_percent'] = (df['variance'] / df['budgeted_cost']) * 100
df['status'] = df['variance'].apply(lambda x: 'Over Budget' if x > 0 else 'Under Budget' if x < 0 else 'On Budget')

# ===== FUNÇÕES =====
def create_sunburst(filtered_df):
    """Cria gráfico sunburst SIMPLES mas FUNCIONANDO"""
    if filtered_df.empty:
        return html.Div("📊 Sem dados para mostrar", style={'textAlign': 'center', 'padding': '50px'})
    
    # Criar estrutura simples para sunburst
    df_hier = []
    
    # Adicionar todos os níveis hierárquicos
    for _, row in filtered_df.iterrows():
        # Pillar (nível 1)
        df_hier.append({
            'ids': row['pillar'],
            'labels': row['pillar'],
            'parents': '',
            'values': 0
        })
        
        # Area (nível 2)
        area_id = f"{row['pillar']} - {row['area']}"
        df_hier.append({
            'ids': area_id,
            'labels': row['area'],
            'parents': row['pillar'],
            'values': 0
        })
        
        # Service (nível 3)
        service_id = f"{area_id} - {row['service']}"
        df_hier.append({
            'ids': service_id,
            'labels': row['service'],
            'parents': area_id,
            'values': 0
        })
        
        # Task (nível 4)  
        task_id = f"{service_id} - {row['task']}"
        df_hier.append({
            'ids': task_id,
            'labels': row['task'],
            'parents': service_id,
            'values': 0
        })
        
        # Sub-task (nível 5 - folhas com valores)
        subtask_id = f"{task_id} - {row['sub_task']}"
        df_hier.append({
            'ids': subtask_id,
            'labels': row['sub_task'],
            'parents': task_id,
            'values': row['cost']
        })
    
    # Remover duplicatas
    df_final = pd.DataFrame(df_hier).drop_duplicates(subset=['ids'])
    
    # Criar figura
    fig = go.Figure(go.Sunburst(
        ids=df_final['ids'],
        labels=df_final['labels'],
        parents=df_final['parents'],
        values=df_final['values'],
        branchvalues="total",
        hovertemplate='<b>%{label}</b><br>Custo: $%{value:,.0f}<extra></extra>',
        maxdepth=4
    ))
    
    fig.update_layout(
        title="☀️ Sunburst - Custos de Construção",
        height=600,
        font=dict(size=12)
    )
    
    return dcc.Graph(figure=fig)

def create_bar_chart(filtered_df):
    """Cria gráfico de barras SIMPLES mas FUNCIONANDO"""
    if filtered_df.empty:
        return html.Div("📊 Sem dados para mostrar", style={'textAlign': 'center', 'padding': '50px'})
    
    pillar_data = filtered_df.groupby('pillar').agg({
        'cost': 'sum',
        'budgeted_cost': 'sum'
    }).reset_index()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Custo Real', x=pillar_data['pillar'], y=pillar_data['cost'], marker_color='#3498db'))
    fig.add_trace(go.Bar(name='Orçamento', x=pillar_data['pillar'], y=pillar_data['budgeted_cost'], marker_color='#27ae60'))
    
    fig.update_layout(
        title="💰 Custo Real vs Orçamento por Pilar",
        barmode='group',
        height=400,
        yaxis_title="Valor ($)",
        xaxis_title="Pilares"
    )
    
    return dcc.Graph(figure=fig)

def create_treemap(filtered_df):
    """Cria treemap SIMPLES mas FUNCIONANDO"""
    if filtered_df.empty:
        return html.Div("📊 Sem dados para mostrar", style={'textAlign': 'center', 'padding': '50px'})
    
    fig = px.treemap(
        filtered_df,
        path=[px.Constant("Projeto"), 'pillar', 'area', 'service', 'sub_task'],
        values='cost',
        color='variance_percent',
        color_continuous_scale='RdYlGn_r',
        title="🗺️ TreeMap - Análise de Custos"
    )
    
    fig.update_layout(height=600)
    return dcc.Graph(figure=fig)

def create_table(filtered_df):
    """Cria tabela SIMPLES mas FUNCIONANDO"""
    if filtered_df.empty:
        return html.Div("📊 Sem dados para mostrar", style={'textAlign': 'center', 'padding': '50px'})
    
    # Preparar dados para tabela (SEM formatação complexa)
    table_df = filtered_df[['pillar', 'area', 'service', 'sub_task', 'cost', 'budgeted_cost', 'variance', 'status']].copy()
    
    return html.Div([
        html.H3("📋 Tabela de Custos", style={'textAlign': 'center', 'marginBottom': '20px'}),
        dash_table.DataTable(
            data=table_df.to_dict('records'),
            columns=[
                {"name": "Pilar", "id": "pillar"},
                {"name": "Área", "id": "area"},
                {"name": "Serviço", "id": "service"},
                {"name": "Sub-tarefa", "id": "sub_task"},
                {"name": "Custo", "id": "cost", "type": "numeric", "format": {"specifier": "$,.0f"}},
                {"name": "Orçamento", "id": "budgeted_cost", "type": "numeric", "format": {"specifier": "$,.0f"}},
                {"name": "Variação", "id": "variance", "type": "numeric", "format": {"specifier": "$,.0f"}},
                {"name": "Status", "id": "status"}
            ],
            style_cell={'textAlign': 'left', 'padding': '10px'},
            style_header={'backgroundColor': '#3498db', 'color': 'white', 'fontWeight': 'bold'},
            page_size=15,
            sort_action='native'
        )
    ])

# ===== APLICATIVO DASH =====
app = Dash(__name__)
app.title = "Sunburst Cost Explorer - FUNCIONANDO"

# Layout SUPER SIMPLES
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("🏗️ Explorador de Custos de Construção", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'})
    ], style={'padding': '20px', 'backgroundColor': '#ecf0f1', 'marginBottom': '20px'}),
    
    # Controles SIMPLES
    html.Div([
        html.Div([
            html.Label("Filtrar por Pilar:", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
            dcc.Dropdown(
                id='pillar-filter-simple',
                options=[{'label': 'Todos', 'value': 'all'}] + 
                        [{'label': p, 'value': p} for p in df['pillar'].unique()],
                value='all'
            )
        ], style={'width': '48%', 'display': 'inline-block', 'marginRight': '4%'}),
        
        html.Div([
            html.Label("Nível de Detalhe:", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
            dcc.Slider(
                id='depth-slider-simple',
                min=2, max=5, step=1, value=4,
                marks={i: f'Nível {i}' for i in range(2, 6)},
                tooltip={"placement": "bottom", "always_visible": True}
            )
        ], style={'width': '48%', 'display': 'inline-block'})
    ], style={'marginBottom': '30px', 'padding': '20px', 'backgroundColor': '#f8f9fa'}),
    
    # Cards de métricas
    html.Div([
        html.Div([
            html.H2(f"${df['cost'].sum():,.0f}", style={'color': '#3498db', 'margin': '0'}),
            html.P("Custo Total", style={'margin': '5px 0 0 0'})
        ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': 'white', 
                 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
        
        html.Div([
            html.H2(f"${df['budgeted_cost'].sum():,.0f}", style={'color': '#27ae60', 'margin': '0'}),
            html.P("Orçamento Total", style={'margin': '5px 0 0 0'})
        ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': 'white', 
                 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
        
        html.Div([
            html.H2(f"${df['variance'].sum():,.0f}", style={'color': '#e74c3c', 'margin': '0'}),
            html.P("Variação Total", style={'margin': '5px 0 0 0'})
        ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': 'white', 
                 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})
    ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr 1fr', 'gap': '20px', 'marginBottom': '30px'}),
    
    # Abas FUNCIONAIS
    dcc.Tabs(id="tabs-simple", value='sunburst', children=[
        dcc.Tab(label='🌞 Sunburst', value='sunburst'),
        dcc.Tab(label='📊 Barras', value='bar'),
        dcc.Tab(label='🗺️ TreeMap', value='treemap'),
        dcc.Tab(label='📋 Tabela', value='table')
    ]),
    
    # Conteúdo das abas
    html.Div(id='tab-content-simple')
    
], style={'margin': '20px', 'fontFamily': 'Arial, sans-serif'})

# ===== CALLBACK ÚNICO E SIMPLES =====
@app.callback(
    Output('tab-content-simple', 'children'),
    [Input('tabs-simple', 'value'),
     Input('pillar-filter-simple', 'value'),
     Input('depth-slider-simple', 'value')]
)
def update_content(active_tab, pillar_filter, depth_level):
    # Filtrar dados
    filtered_df = df.copy()
    
    if pillar_filter != 'all':
        filtered_df = filtered_df[filtered_df['pillar'] == pillar_filter]
    
    # Criar conteúdo baseado na aba ativa
    if active_tab == 'sunburst':
        return create_sunburst(filtered_df)
    elif active_tab == 'bar':
        return create_bar_chart(filtered_df)
    elif active_tab == 'treemap':
        return create_treemap(filtered_df)
    elif active_tab == 'table':
        return create_table(filtered_df)
    else:
        return html.Div("Selecione uma aba")

# ===== EXECUTAR =====
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8052)

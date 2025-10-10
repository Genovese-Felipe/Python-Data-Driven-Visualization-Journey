
#!/usr/bin/env python3
"""An advanced Dash dashboard for exploring residential construction costs.

This script creates a standalone Dash application that provides an interactive
interface for analyzing a simplified construction cost dataset. It is designed
to showcase best practices in building interactive Plotly dashboards.

The dashboard features:
- A clear header with a title and subtitle.
- Summary metric cards for total cost, total budget, and total variance.
- A dropdown filter to narrow the data by project pillar.
- A sunburst chart for visualizing the hierarchical distribution of costs.
- A bar chart that compares the actual cost vs. the budgeted cost for the
  selected pillar(s).
"""

print("🚀 Iniciando Explorador Avançado de Custos de Construção... / Starting Advanced Construction Cost Explorer...")

try:
    from dash import Dash, html, dcc, callback, dash_table
    from dash.dependencies import Input, Output
    import plotly.express as px
    import pandas as pd
    import plotly.graph_objects as go
    import numpy as np
    
    print("✅ Todas as dependências carregadas com sucesso!")
    
    # Dados principais (versão simplificada do original)
    data = [
        {'pillar': 'Project Design', 'area': 'Architecture', 'service': 'Blueprint Design', 'cost': 65000, 'budgeted_cost': 60000},
        {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'Structural Analysis', 'cost': 95000, 'budgeted_cost': 91000},
        {'pillar': 'Management', 'area': 'Administration', 'service': 'Project Management', 'cost': 220000, 'budgeted_cost': 214000},
        {'pillar': 'Management', 'area': 'Logistics', 'service': 'Supply Chain', 'cost': 125000, 'budgeted_cost': 120000},
        {'pillar': 'Construction', 'area': 'Site & Foundation', 'service': 'Excavation & Grading', 'cost': 470000, 'budgeted_cost': 460000},
        {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Electrical', 'cost': 500000, 'budgeted_cost': 485000},
        {'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Cabinetry & Countertops', 'cost': 220000, 'budgeted_cost': 210000},
    ]
    
    df = pd.DataFrame(data)
    df['variance'] = df['cost'] - df['budgeted_cost']
    df['variance_percent'] = (df['variance'] / df['budgeted_cost']) * 100
    
    app = Dash(__name__)
    """The main Dash application instance for the advanced cost explorer."""
    app.title = "Explorador de Custos de Construção"
    
    app.layout = html.Div([
        # The main container for the app's layout.

        # Header section with a title and subtitle.
        html.Div([
            html.H1("🏗️ Explorador Avançado de Custos de Construção Residencial",
                   style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '20px'}),
            html.P("Análise interativa baseada nas melhores práticas Plotly",
                  style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '1.2em'})
        ], style={'backgroundColor': '#ecf0f1', 'padding': '30px', 'borderRadius': '10px', 'marginBottom': '20px'}),
        
        # Container for the summary metric cards.
        html.Div([
            # Card for Total Cost.
            html.Div([
                html.H3(f"${df['cost'].sum():,.0f}", style={'color': '#3498db', 'margin': '0', 'fontSize': '2em'}),
                html.P("Custo Total Real", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center', 'backgroundColor': '#ffffff', 'padding': '20px', 'borderRadius': '8px', 'width': '200px', 'margin': '10px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
            
            # Card for Total Budget.
            html.Div([
                html.H3(f"${df['budgeted_cost'].sum():,.0f}", style={'color': '#95a5a6', 'margin': '0', 'fontSize': '2em'}),
                html.P("Orçamento Total", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center', 'backgroundColor': '#ffffff', 'padding': '20px', 'borderRadius': '8px', 'width': '200px', 'margin': '10px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
            
            # Card for Total Variance.
            html.Div([
                html.H3(f"${df['variance'].sum():,.0f}", style={'color': '#e74c3c', 'margin': '0', 'fontSize': '2em'}),
                html.P("Variação Total", style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center', 'backgroundColor': '#ffffff', 'padding': '20px', 'borderRadius': '8px', 'width': '200px', 'margin': '10px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
        ], style={'display': 'flex', 'justifyContent': 'center', 'marginBottom': '30px'}),
        
        # Container for the filter controls.
        html.Div([
            html.Label("Filtrar por Pilar:", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
            dcc.Dropdown(
                id='pillar-filter',
                options=[{'label': 'Todos os Pilares', 'value': 'all'}] + 
                        [{'label': pillar, 'value': pillar} for pillar in df['pillar'].unique()],
                value='all',
                style={'marginBottom': '20px'}
            ),
        ], style={'width': '300px', 'margin': '0 auto', 'marginBottom': '30px'}),
        
        # Placeholders for the sunburst and bar charts.
        dcc.Graph(id='sunburst-chart'),
        dcc.Graph(id='bar-chart'),
        
        # A simple status message at the bottom of the app.
        html.Div([
            html.P("✅ Aplicativo carregado com sucesso!", 
                   style={'textAlign': 'center', 'color': '#27ae60', 'fontSize': '18px', 'fontWeight': 'bold'}),
            html.P("🚀 Todas as funcionalidades estão operacionais", 
                   style={'textAlign': 'center', 'color': '#3498db', 'fontSize': '14px'})
        ], style={'marginTop': '30px', 'padding': '20px', 'backgroundColor': '#e8f6f3', 'borderRadius': '8px'})
    ], style={'fontFamily': 'Arial, sans-serif', 'margin': '20px'})
    
    @app.callback(
        [Output('sunburst-chart', 'figure'),
         Output('bar-chart', 'figure')],
        [Input('pillar-filter', 'value')]
    )
    def update_charts(pillar_filter):
        """Updates the sunburst and bar charts based on the selected pillar.

        This callback filters the DataFrame based on the pillar selected in the
        dropdown. It then generates a new sunburst chart for hierarchical
        cost distribution and a bar chart comparing actual vs. budgeted
        costs for the filtered data.

        Args:
            pillar_filter (str): The pillar selected from the dropdown.

        Returns:
            tuple: A tuple containing two Plotly Figure objects:
                - fig_sunburst: The updated sunburst chart.
                - fig_bar: The updated bar chart.
        """
        filtered_df = df if pillar_filter == 'all' else df[df['pillar'] == pillar_filter]
        
        # Sunburst
        fig_sunburst = px.sunburst(
            filtered_df,
            path=[px.Constant("Projeto"), 'pillar', 'area', 'service'],
            values='cost',
            title='Análise Sunburst: Distribuição Hierárquica de Custos',
            height=600
        )
        fig_sunburst.update_layout(font={'family': 'Arial, sans-serif'})
        
        # Barras
        pillar_summary = filtered_df.groupby('pillar').agg({
            'cost': 'sum',
            'budgeted_cost': 'sum'
        }).reset_index()
        
        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(x=pillar_summary['pillar'], y=pillar_summary['cost'], 
                                name='Custo Real', marker_color='#3498db'))
        fig_bar.add_trace(go.Bar(x=pillar_summary['pillar'], y=pillar_summary['budgeted_cost'], 
                                name='Orçamento', marker_color='#95a5a6'))
        fig_bar.update_layout(
            title='Comparação: Custo Real vs Orçamento por Pilar',
            xaxis_title='Pilares',
            yaxis_title='Valor ($)',
            barmode='group',
            height=500,
            font={'family': 'Arial, sans-serif'}
        )
        
        return fig_sunburst, fig_bar
    
    print("🌐 Iniciando servidor Dash...")
    print("📊 Acesse: http://localhost:8050")
    app.run_server(debug=True, port=8050, host='0.0.0.0')
    
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()

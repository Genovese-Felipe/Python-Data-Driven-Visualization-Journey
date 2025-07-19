#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sunburst Cost Explorer - Versão Funcional
Baseado nos dados extraídos do HTML de referência
"""

import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

# Dados extraídos do HTML de referência
labels = ["Invoicing","HVAC Installation","Layout Planning","Lighting Fixtures","Load Bearing Calculations","Machinery Rental","Material Sourcing","Painting","Patio and Walkway Construction","Permit Application","Planting and Tree Installation","Hardwood Installation","Plumbing Installation","Progress Reporting","Retaining Wall Construction","Shingle Installation","Site Survey","Pouring","Lawn Installation","Soil Testing","Steel Erection","Tiling","Tool Rental","Underlayment","Window Installation","Wood Framing","Wiring Installation","HVAC Design","Grading Plan","Excavation","Cabinetry Installation","Fixture Installation","Curing","Daily Supervision","Drywall Installation","Detailed Drawings","Door Installation","Drainage Design","Electrical Design","Delivery Coordination","Budget Monitoring","Budget Tracking & Invoicing","City & Environmental Approvals","Complete Wiring & Fixtures","Drainage & Grading Plan","Earthwork and Site Prep","Exterior and Interior Openings","Foundation & Frame Calculations","Foundation Pouring & Curing","HVAC & Electrical Plans","Hardwood and Ceramic Installation","Heavy Machinery & Tools","Initial Schematics & 3D Model","Interior Walls and Ceilings","Kitchen and Bathroom Fixtures","Lawn, Plants, and Trees","Lighting, Faucets, and Door Knobs","Material Selection & Layout","On-Site Supervision & Reporting","Patio, Walkways, and Retaining Walls","Piping, Drains & Ductwork","Shingle and Underlayment Installation","Wood & Steel Frame Erection","Blueprint Design","Cabinetry & Countertops","Civil Engineering","Equipment Rental","Electrical","Fixtures & Hardware","Financial Management","Flooring & Tiling","Hardscaping","Interior Design","MarchJEP Engineering","MEP Engineering","Permits & Legal","Plumbing & HVAC","Project Management","Roofing","Softscaping","Structural Analysis","Supply Chain","Window & Door Installation","Administration","Architecture","Engineering","Finishing","Interior & Exterior","Landscaping","Logistics","MEP Systems","Site & Foundation","Superstructure","Construction","Finishing & Landscaping","Management","Project Design"]

parents = ["Management/Administration/Financial Management/Budget Tracking & Invoicing","Construction/MEP Systems/Plumbing & HVAC/Piping, Drains & Ductwork","Project Design/Architecture/Interior Design/Material Selection & Layout","Finishing & Landscaping/Finishing/Fixtures & Hardware/Lighting, Faucets, and Door Knobs","Project Design/Engineering/Structural Analysis/Foundation & Frame Calculations","Management/Logistics/Equipment Rental/Heavy Machinery & Tools","Management/Logistics/Supply Chain/Material Sourcing & Delivery","Construction/Interior & Exterior/Drywall & Painting/Interior Walls and Ceilings","Finishing & Landscaping/Landscaping/Hardscaping/Patio, Walkways, and Retaining Walls","Management/Administration/Permits & Legal/City & Environmental Approvals","Finishing & Landscaping/Landscaping/Softscaping/Lawn, Plants, and Trees","Construction/Interior & Exterior/Flooring & Tiling/Hardwood and Ceramic Installation","Construction/MEP Systems/Plumbing & HVAC/Piping, Drains & Ductwork","Management/Administration/Project Management/On-Site Supervision & Reporting","Finishing & Landscaping/Landscaping/Hardscaping/Patio, Walkways, and Retaining Walls","Construction/Superstructure/Roofing/Shingle and Underlayment Installation","Project Design/Engineering/Civil Engineering/Drainage & Grading Plan","Construction/Site & Foundation/Concrete Work/Foundation Pouring & Curing","Finishing & Landscaping/Landscaping/Softscaping/Lawn, Plants, and Trees","Project Design/Engineering/Structural Analysis/Foundation & Frame Calculations","Construction/Superstructure/Framing & Steel/Wood & Steel Frame Erection","Construction/Interior & Exterior/Flooring & Tiling/Hardwood and Ceramic Installation","Management/Logistics/Equipment Rental/Heavy Machinery & Tools","Construction/Superstructure/Roofing/Shingle and Underlayment Installation","Construction/Interior & Exterior/Window & Door Installation/Exterior and Interior Openings","Construction/Superstructure/Framing & Steel/Wood & Steel Frame Erection","Construction/MEP Systems/Electrical/Complete Wiring & Fixtures","Project Design/Engineering/MarchJEP Engineering/HVAC & Electrical Plans","Project Design/Engineering/Civil Engineering/Drainage & Grading Plan","Construction/Site & Foundation/Excavation & Grading/Earthwork and Site Prep","Finishing & Landscaping/Finishing/Cabinetry & Countertops/Kitchen and Bathroom Fixtures","Construction/MEP Systems/Electrical/Complete Wiring & Fixtures","Construction/Site & Foundation/Concrete Work/Foundation Pouring & Curing","Management/Administration/Project Management/On-Site Supervision & Reporting","Construction/Interior & Exterior/Drywall & Painting/Interior Walls and Ceilings","Project Design/Architecture/Blueprint Design/Initial Schematics & 3D Model","Construction/Interior & Exterior/Window & Door Installation/Exterior and Interior Openings","Project Design/Engineering/Civil Engineering/Drainage & Grading Plan","Project Design/Engineering/MarchJEP Engineering/HVAC & Electrical Plans","Management/Logistics/Supply Chain/Material Sourcing & Delivery","Management/Administration/Financial Management/Budget Tracking & Invoicing","Management/Administration/Financial Management/Budget Tracking & Invoicing","Management/Administration/Permits & Legal/City & Environmental Approvals","Construction/MEP Systems/Electrical/Complete Wiring & Fixtures","Project Design/Engineering/Civil Engineering/Drainage & Grading Plan","Construction/Site & Foundation/Excavation & Grading/Earthwork and Site Prep","Construction/Interior & Exterior/Window & Door Installation/Exterior and Interior Openings","Project Design/Engineering/Structural Analysis/Foundation & Frame Calculations","Construction/Site & Foundation/Concrete Work/Foundation Pouring & Curing","Project Design/Engineering/MarchJEP Engineering/HVAC & Electrical Plans","Construction/Interior & Exterior/Flooring & Tiling/Hardwood and Ceramic Installation","Management/Logistics/Equipment Rental/Heavy Machinery & Tools","Project Design/Architecture/Blueprint Design/Initial Schematics & 3D Model","Construction/Interior & Exterior/Drywall & Painting/Interior Walls and Ceilings","Finishing & Landscaping/Finishing/Cabinetry & Countertops/Kitchen and Bathroom Fixtures","Finishing & Landscaping/Landscaping/Softscaping/Lawn, Plants, and Trees","Finishing & Landscaping/Finishing/Fixtures & Hardware/Lighting, Faucets, and Door Knobs","Project Design/Architecture/Interior Design/Material Selection & Layout","Management/Administration/Project Management/On-Site Supervision & Reporting","Finishing & Landscaping/Landscaping/Hardscaping/Patio, Walkways, and Retaining Walls","Construction/MEP Systems/Plumbing & HVAC/Piping, Drains & Ductwork","Construction/Superstructure/Roofing/Shingle and Underlayment Installation","Construction/Superstructure/Framing & Steel/Wood & Steel Frame Erection","Project Design/Architecture/Blueprint Design","Finishing & Landscaping/Finishing/Cabinetry & Countertops","Project Design/Engineering/Civil Engineering","Management/Logistics/Equipment Rental","Construction/MEP Systems/Electrical","Finishing & Landscaping/Finishing/Fixtures & Hardware","Management/Administration/Financial Management","Construction/Interior & Exterior/Flooring & Tiling","Finishing & Landscaping/Landscaping/Hardscaping","Project Design/Architecture/Interior Design","Project Design/Engineering/MEP Engineering","Project Design/Engineering/MEP Engineering","Management/Administration/Permits & Legal","Construction/MEP Systems/Plumbing & HVAC","Management/Administration/Project Management","Construction/Superstructure/Roofing","Finishing & Landscaping/Landscaping/Softscaping","Project Design/Engineering/Structural Analysis","Management/Logistics/Supply Chain","Construction/Interior & Exterior/Window & Door Installation","Management/Administration","Project Design/Architecture","Project Design/Engineering","Finishing & Landscaping/Finishing","Construction/Interior & Exterior","Finishing & Landscaping/Landscaping","Management/Logistics","Construction/MEP Systems","Construction/Site & Foundation","Construction/Superstructure","Construction","Finishing & Landscaping","Management","Project Design"]

values = [310000,85000,175000,55000,65000,190000,150000,40000,70000,40000,70000,130000,80000,260000,120000,480000,65000,150000,30000,310000,190000,240000,55000,160000,60000,70000,175000,480000,80000,40000,85000,90000,260000,130000,120000,40000,95000,70000,90000,280000,105000,210000,220000,455000,120000,125000,500000,470000,600000,2025000,340000,405000,315000]

# Cores baseadas no HTML de referência
colors = ["#d62728","#1f77b4","#ff7f0e","#ff7f0e","#d62728","#2ca02c","#2ca02c","#2ca02c","#1f77b4","#d62728","#1f77b4","#2ca02c","#2ca02c","#2ca02c","#ff7f0e","#2ca02c","#ff7f0e","#d62728","#2ca02c","#2ca02c","#d62728","#1f77b4","#1f77b4","#ff7f0e","#2ca02c","#ff7f0e","#2ca02c","#d62728","#1f77b4","#ff7f0e","#2ca02c","#ff7f0e","#1f77b4","#1f77b4","#d62728","#2ca02c","#d62728","#ff7f0e","#2ca02c","#2ca02c","#2ca02c","#2ca02c","#d62728","#ff7f0e","#1f77b4"]

# Inicialização do app Dash
app = dash.Dash(__name__)
app.title = "🏗️ Explorador de Custos de Construção - Sunburst"

# Layout da aplicação
app.layout = html.Div([
    html.Div([
        html.H1("🏗️ Explorador de Custos de Construção", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}),
        
        html.Div([
            html.P("Análise interativa de custos hierárquicos de construção residencial", 
                   style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '18px'})
        ], style={'marginBottom': '30px'}),
        
        # Gráfico Sunburst principal
        dcc.Graph(id='sunburst-chart'),
        
        # Métricas resumidas
        html.Div(id='summary-metrics', style={'marginTop': '30px'}),
        
    ], style={
        'padding': '20px',
        'maxWidth': '1200px',
        'margin': '0 auto',
        'fontFamily': 'Arial, sans-serif'
    })
])

# Callback para criar o gráfico sunburst
@app.callback(
    Output('sunburst-chart', 'figure'),
    Input('sunburst-chart', 'id')  # Trigger inicial
)
def create_sunburst_chart(_):
    """Cria o gráfico sunburst com os dados funcionais."""
    
    fig = go.Figure(go.Sunburst(
        labels=labels,
        parents=parents,
        values=values,
        branchvalues="total",
        hovertemplate='<b>%{label}</b><br>Custo: $%{value:,.0f}<br>Percentual: %{percentParent}<extra></extra>',
        maxdepth=4,
        insidetextorientation='radial'
    ))
    
    fig.update_layout(
        title={
            'text': "Distribuição Hierárquica de Custos de Construção",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'family': 'Arial, sans-serif', 'color': '#2c3e50'}
        },
        font=dict(size=12),
        paper_bgcolor='white',
        plot_bgcolor='white',
        height=700,
        margin=dict(t=80, l=20, r=20, b=20)
    )
    
    return fig

# Callback para métricas resumidas
@app.callback(
    Output('summary-metrics', 'children'),
    Input('sunburst-chart', 'id')  # Trigger inicial
)
def create_summary_metrics(_):
    """Cria métricas resumidas dos custos."""
    
    total_cost = sum(values)
    
    return html.Div([
        html.H3("📊 Resumo Financeiro", style={'color': '#2c3e50', 'textAlign': 'center'}),
        
        html.Div([
            html.Div([
                html.H4(f"${total_cost:,.0f}", style={'color': '#e74c3c', 'margin': '0'}),
                html.P("Custo Total", style={'margin': '5px 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#f8f9fa', 'borderRadius': '8px'}),
            
            html.Div([
                html.H4(f"{len([v for v in values if v > 0])}", style={'color': '#3498db', 'margin': '0'}),
                html.P("Itens de Custo", style={'margin': '5px 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#f8f9fa', 'borderRadius': '8px'}),
            
            html.Div([
                html.H4(f"${max(values):,.0f}", style={'color': '#f39c12', 'margin': '0'}),
                html.P("Maior Custo", style={'margin': '5px 0', 'color': '#7f8c8d'})
            ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#f8f9fa', 'borderRadius': '8px'}),
            
        ], style={
            'display': 'flex',
            'justifyContent': 'space-around',
            'gap': '20px',
            'marginTop': '20px'
        })
    ])

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8052)

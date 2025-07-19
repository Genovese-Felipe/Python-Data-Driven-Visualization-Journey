
# Advanced Residential Construction Cost Explorer with Enhanced Plotly Visualization
# Baseado nas melhores práticas dos guias Plotly para Python
# Aplicando técnicas avançadas de visualização conforme os guias XML

from dash import Dash, dcc, html, dash_table, callback
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
	# New Pillar: Finishing & Landscaping
	{'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Cabinetry & Countertops', 'task': 'Kitchen and Bathroom Fixtures', 'sub_task': 'Cabinetry Installation', 'cost': 90000, 'budgeted_cost': 88000},
	{'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Cabinetry & Countertops', 'task': 'Kitchen and Bathroom Fixtures', 'sub_task': 'Countertop Installation', 'cost': 60000, 'budgeted_cost': 58000},
	{'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Fixtures & Hardware', 'task': 'Lighting, Faucets, and Door Knobs', 'sub_task': 'Lighting Fixtures', 'cost': 35000, 'budgeted_cost': 34000},
	{'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Fixtures & Hardware', 'task': 'Lighting, Faucets, and Door Knobs', 'sub_task': 'Faucets and Hardware', 'cost': 35000, 'budgeted_cost': 33000},
	{'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Hardscaping', 'task': 'Patio, Walkways, and Retaining Walls', 'sub_task': 'Patio and Walkway Construction', 'cost': 50000, 'budgeted_cost': 48000},
	{'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Hardscaping', 'task': 'Patio, Walkways, and Retaining Walls', 'sub_task': 'Retaining Wall Construction', 'cost': 30000, 'budgeted_cost': 29000},
	{'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Softscaping', 'task': 'Lawn, Plants, and Trees', 'sub_task': 'Lawn Installation', 'cost': 20000, 'budgeted_cost': 19000},
	{'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Softscaping', 'task': 'Lawn, Plants, and Trees', 'sub_task': 'Planting and Tree Installation', 'cost': 20000, 'budgeted_cost': 18000}
]

# Criar DataFrame com colunas adicionais para análise aprimorada
df_budget = pd.DataFrame(data)
# Adicionar métricas calculadas para análise avançada
df_budget['variance'] = df_budget['cost'] - df_budget['budgeted_cost']
df_budget['variance_percent'] = (df_budget['variance'] / df_budget['budgeted_cost']) * 100
df_budget['status'] = df_budget['variance'].apply(lambda x: 'Over Budget' if x > 0 else 'Under Budget' if x < 0 else 'On Budget')
df_budget['risk_level'] = df_budget['variance_percent'].apply(lambda x: 'High Risk' if abs(x) > 10 else 'Medium Risk' if abs(x) > 5 else 'Low Risk')
min_cost = df_budget['cost'].min()
max_cost = df_budget['cost'].max()


# Paletas de cores personalizadas baseadas nos guias
CUSTOM_COLORS = {
	'pillar': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
	'status': {'Over Budget': '#e74c3c', 'Under Budget': '#27ae60', 'On Budget': '#3498db'},
	'risk': {'High Risk': '#e74c3c', 'Medium Risk': '#f39c12', 'Low Risk': '#27ae60'},
	'sequential': px.colors.sequential.Viridis,
	'diverging': px.colors.diverging.RdYlBu
}

# Dicionário de cores para pilares (usado em gráficos)
pillar_colors = {
	'Project Design': '#1f77b4',
	'Management': '#ff7f0e',
	'Construction': '#2ca02c',
	'Finishing & Landscaping': '#d62728'
}

# Função para criar hierarquia conforme especificado nos guias
def create_hierarchy_paths(df):
	"""Cria caminhos hierárquicos para sunburst seguindo as melhores práticas dos guias."""
	df = df.copy()
	df['ids'] = df['pillar'] + ' - ' + df['area'] + ' - ' + df['service'] + ' - ' + df['task'] + ' - ' + df['sub_task']
	df['parents'] = df['pillar'] + ' - ' + df['area'] + ' - ' + df['service'] + ' - ' + df['task']
	
	# Criar níveis hierárquicos
	hierarchy_data = []
	
	# Nível 1: Pillars
	for pillar in df['pillar'].unique():
		pillar_data = df[df['pillar'] == pillar]
		hierarchy_data.append({
			'ids': pillar,
			'labels': pillar,
			'parents': '',
			'values': pillar_data['cost'].sum(),
			'budgeted_values': pillar_data['budgeted_cost'].sum(),
			'level': 1
		})
	
	# Nível 2: Areas
	for _, row in df.groupby(['pillar', 'area']).first().reset_index().iterrows():
		area_data = df[(df['pillar'] == row['pillar']) & (df['area'] == row['area'])]
		hierarchy_data.append({
			'ids': row['pillar'] + ' - ' + row['area'],
			'labels': row['area'],
			'parents': row['pillar'],
			'values': area_data['cost'].sum(),
			'budgeted_values': area_data['budgeted_cost'].sum(),
			'level': 2
		})
	
	# Nível 3: Services
	for _, row in df.groupby(['pillar', 'area', 'service']).first().reset_index().iterrows():
		service_data = df[(df['pillar'] == row['pillar']) & 
						 (df['area'] == row['area']) & 
						 (df['service'] == row['service'])]
		hierarchy_data.append({
			'ids': row['pillar'] + ' - ' + row['area'] + ' - ' + row['service'],
			'labels': row['service'],
			'parents': row['pillar'] + ' - ' + row['area'],
			'values': service_data['cost'].sum(),
			'budgeted_values': service_data['budgeted_cost'].sum(),
			'level': 3
		})
	
	# Nível 4: Tasks
	for _, row in df.groupby(['pillar', 'area', 'service', 'task']).first().reset_index().iterrows():
		task_data = df[(df['pillar'] == row['pillar']) & 
					  (df['area'] == row['area']) & 
					  (df['service'] == row['service']) &
					  (df['task'] == row['task'])]
		hierarchy_data.append({
			'ids': row['pillar'] + ' - ' + row['area'] + ' - ' + row['service'] + ' - ' + row['task'],
			'labels': row['task'],
			'parents': row['pillar'] + ' - ' + row['area'] + ' - ' + row['service'],
			'values': task_data['cost'].sum(),
			'budgeted_values': task_data['budgeted_cost'].sum(),
			'level': 4
		})
	
	# Nível 5: Sub-tasks (folhas)
	for _, row in df.iterrows():
		hierarchy_data.append({
			'ids': row['ids'],
			'labels': row['sub_task'],
			'parents': row['parents'],
			'values': row['cost'],
			'budgeted_values': row['budgeted_cost'],
			'level': 5
		})
	
	return pd.DataFrame(hierarchy_data)
# Inicializar aplicativo Dash com customizações avançadas
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Advanced Construction Cost Explorer"

# CSS customizado conforme as melhores práticas dos guias
app.layout = html.Div([
	# Header principal com estilo profissional
	html.Div([
		html.H1(
			"Explorador Avançado de Custos de Construção Residencial",
			style={
				'textAlign': 'center',
				'color': '#2c3e50',
				'marginBottom': '10px',
				'fontFamily': 'Arial, sans-serif',
				'fontSize': '2.5em',
				'fontWeight': 'bold'
			}
		),
		html.P(
			"Análise interativa hierárquica com visualizações avançadas baseadas nas melhores práticas Plotly",
			style={
				'textAlign': 'center',
				'color': '#7f8c8d',
				'marginBottom': '30px',
				'fontFamily': 'Arial, sans-serif',
				'fontSize': '1.2em'
			}
		),
	], style={
		'backgroundColor': '#ecf0f1',
		'padding': '30px',
		'marginBottom': '20px',
		'borderRadius': '10px',
		'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
	}),
	
	# Painel de controles principais
	html.Div([
		html.Div([
			html.Label("Selecionar Métrica para Análise:", 
					  style={'fontWeight': 'bold', 'marginBottom': '10px', 'fontFamily': 'Arial, sans-serif'}),
			dcc.Dropdown(
				id='metric-dropdown',
				options=[
					{'label': 'Custo Real', 'value': 'values'},
					{'label': 'Orçamento Planejado', 'value': 'budgeted_values'},
					{'label': 'Variação Absoluta', 'value': 'variance'}
				],
				value='values',
				style={'marginBottom': '20px'}
			),
		], style={'width': '30%', 'display': 'inline-block', 'marginRight': '5%'}),
		
		html.Div([
			html.Label("Filtrar por Pilar:", 
					  style={'fontWeight': 'bold', 'marginBottom': '10px', 'fontFamily': 'Arial, sans-serif'}),
			dcc.Dropdown(
				id='pillar-filter',
				options=[{'label': 'Todos os Pilares', 'value': 'all'}] + 
						[{'label': pillar, 'value': pillar} for pillar in df_budget['pillar'].unique()],
				value='all',
				style={'marginBottom': '20px'}
			),
		], style={'width': '30%', 'display': 'inline-block', 'marginRight': '5%'}),
		
		html.Div([
			html.Label("Nível de Detalhe:", 
					  style={'fontWeight': 'bold', 'marginBottom': '10px', 'fontFamily': 'Arial, sans-serif'}),
			dcc.Slider(
				id='depth-slider',
				min=2,
				max=5,
				step=1,
				value=4,
				marks={i: f'Nível {i}' for i in range(2, 6)},
				tooltip={"placement": "bottom", "always_visible": True}
			),
		], style={'width': '30%', 'display': 'inline-block'}),
	], style={
		'backgroundColor': '#f8f9fa',
		'padding': '20px',
		'marginBottom': '20px',
		'borderRadius': '8px',
		'border': '1px solid #dee2e6'
	}),
	
	# Métricas resumo em cards
	html.Div([
		html.Div([
			html.H3(f"${df_budget['cost'].sum():,.0f}", 
				   style={'color': '#3498db', 'margin': '0', 'fontSize': '2em'}),
			html.P("Custo Total Real", 
				  style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
		], style={
			'textAlign': 'center', 'backgroundColor': '#ffffff', 'padding': '20px',
			'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
			'border': '1px solid #e9ecef'
		}, className='metric-card'),
		
		html.Div([
			html.H3(f"${df_budget['budgeted_cost'].sum():,.0f}", 
				   style={'color': '#95a5a6', 'margin': '0', 'fontSize': '2em'}),
			html.P("Orçamento Total", 
				  style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
		], style={
			'textAlign': 'center', 'backgroundColor': '#ffffff', 'padding': '20px',
			'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
			'border': '1px solid #e9ecef'
		}, className='metric-card'),
		
		html.Div([
			html.H3(f"${df_budget['variance'].sum():,.0f}", 
				   style={'color': '#e74c3c' if df_budget['variance'].sum() > 0 else '#27ae60', 
						 'margin': '0', 'fontSize': '2em'}),
			html.P("Variação Total", 
				  style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
		], style={
			'textAlign': 'center', 'backgroundColor': '#ffffff', 'padding': '20px',
			'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
			'border': '1px solid #e9ecef'
		}, className='metric-card'),
		
		html.Div([
			html.H3(f"{(df_budget['variance'].sum()/df_budget['budgeted_cost'].sum()*100):+.1f}%", 
				   style={'color': '#f39c12', 'margin': '0', 'fontSize': '2em'}),
			html.P("Variação Percentual", 
				  style={'margin': '5px 0 0 0', 'color': '#7f8c8d'})
		], style={
			'textAlign': 'center', 'backgroundColor': '#ffffff', 'padding': '20px',
			'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
			'border': '1px solid #e9ecef'
		}, className='metric-card'),
	], style={
		'display': 'grid',
		'gridTemplateColumns': 'repeat(auto-fit, minmax(200px, 1fr))',
		'gap': '20px',
		'marginBottom': '30px'
	}),
	
	# Abas para diferentes visualizações
	dcc.Tabs(id="visualization-tabs", value='sunburst-tab', children=[
		dcc.Tab(label='Análise Sunburst', value='sunburst-tab', style={'fontFamily': 'Arial, sans-serif'}),
		dcc.Tab(label='Comparação por Barras', value='bar-tab', style={'fontFamily': 'Arial, sans-serif'}),
		dcc.Tab(label='Treemap Hierárquico', value='treemap-tab', style={'fontFamily': 'Arial, sans-serif'}),
		dcc.Tab(label='Tabela Detalhada', value='table-tab', style={'fontFamily': 'Arial, sans-serif'}),
	], style={'marginBottom': '20px'}),
	
	# Container para conteúdo das abas
	html.Div(id='tab-content'),
	
	# Footer informativo
	html.Div([
		html.P([
			"Aplicativo desenvolvido seguindo as melhores práticas dos guias Plotly para Python | ",
			html.A("Documentação Plotly", href="https://plotly.com/python/", target="_blank"),
			" | Versão: 2.0 Advanced"
		], style={
			'textAlign': 'center',
			'color': '#7f8c8d',
			'fontSize': '0.9em',
			'margin': '0'
		})
	], style={
		'backgroundColor': '#ecf0f1',
		'padding': '15px',
		'marginTop': '30px',
		'borderRadius': '8px'
	})
], style={
	'fontFamily': 'Arial, sans-serif',
	'margin': '20px',
	'backgroundColor': '#ffffff'
})


# Inicializar hierarchy_df para uso nos callbacks
hierarchy_df = create_hierarchy_paths(df_budget)

def create_enhanced_sunburst(filtered_df):
	"""Criar gráfico sunburst aprimorado com melhores práticas do Plotly"""
	if filtered_df.empty:
		return html.Div("📊 Nenhum dado disponível para os filtros selecionados", 
					   style={'textAlign': 'center', 'padding': '50px', 'color': '#7f8c8d'})
	# Preparar estrutura hierárquica conforme guias Plotly
	df_hierarchy = []
	# Adicionar níveis hierárquicos
	for _, row in filtered_df.iterrows():
		# Nível 1: Pillar
		df_hierarchy.append({
			'ids': row['pillar'],
			'labels': row['pillar'],
			'parents': '',
			'values': 0  # Será calculado automaticamente
		})
		# Nível 2: Area
		area_id = f"{row['pillar']} - {row['area']}"
		df_hierarchy.append({
			'ids': area_id,
			'labels': row['area'],
			'parents': row['pillar'],
			'values': 0
		})
		# Nível 3: Service
		service_id = f"{area_id} - {row['service']}"
		df_hierarchy.append({
			'ids': service_id,
			'labels': row['service'],
			'parents': area_id,
			'values': 0
		})
		# Nível 4: Task
		task_id = f"{service_id} - {row['task']}"
		df_hierarchy.append({
			'ids': task_id,
			'labels': row['task'],
			'parents': service_id,
			'values': 0
		})
		# Nível 5: Sub-task (folhas com valores)
		subtask_id = f"{task_id} - {row['sub_task']}"
		df_hierarchy.append({
			'ids': subtask_id,
			'labels': row['sub_task'],
			'parents': task_id,
			'values': row['cost']
		})
	# Remover duplicatas mantendo estrutura hierárquica
	hierarchy_df = pd.DataFrame(df_hierarchy).drop_duplicates(subset=['ids'])
	# Definir cores baseadas no pilar
	colors = []
	for label in hierarchy_df['labels']:
		if label in pillar_colors:
			colors.append(pillar_colors[label])
		else:
			colors.append('#95a5a6')  # Cor padrão
	# Criar sunburst com plotly.graph_objects para maior controle
	fig = go.Figure(go.Sunburst(
		ids=hierarchy_df['ids'],
		labels=hierarchy_df['labels'],
		parents=hierarchy_df['parents'],
		values=hierarchy_df['values'],
		branchvalues="total",
		hovertemplate='<b>%{label}</b><br>' +
					 'Custo: $%{value:,.0f}<br>' +
					 'Porcentagem do Total: %{percentRoot:.1%}<br>' +
					 'Porcentagem do Pai: %{percentParent:.1%}<br>' +
					 '<extra></extra>',
		maxdepth=4,
		insidetextorientation='radial'
	))
	# Aplicar configurações avançadas de layout conforme guias
	fig.update_layout(
		title={
			'text': "☀️ Visualização Hierárquica de Custos de Construção",
			'x': 0.5,
			'xanchor': 'center',
			'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
		},
		font=dict(family="Arial, sans-serif", size=12),
		margin=dict(t=100, l=20, r=20, b=20),
		height=700,
		paper_bgcolor='#f8f9fa',
		plot_bgcolor='white'
	)
	return dcc.Graph(figure=fig, config={'displayModeBar': True, 'toImageButtonOptions': {'format': 'png', 'filename': 'sunburst_costs', 'height': 700, 'width': 1000, 'scale': 1}})

def create_enhanced_treemap(filtered_df):
	"""Criar treemap aprimorado seguindo as melhores práticas do Plotly"""
	if filtered_df.empty:
		return html.Div("📊 Nenhum dado disponível para os filtros selecionados", 
					   style={'textAlign': 'center', 'padding': '50px', 'color': '#7f8c8d'})
	
	# Calcular cores baseadas na variação orçamentária
	# Usar escala RdYlGn_r (Red-Yellow-Green reversed) para mostrar problemas em vermelho
	fig = px.treemap(
		filtered_df,
		path=[px.Constant("Projeto de Construção"), 'pillar', 'area', 'service', 'task', 'sub_task'],
		values='cost',
		color='variance_percent',
		color_continuous_scale='RdYlGn_r',  # Vermelho para valores altos (sobre orçamento)
		color_continuous_midpoint=0,
		title="📊 Mapa de Árvore - Análise de Custos vs Orçamento",
		hover_data={
			'cost': ':$,.0f',
			'budgeted_cost': ':$,.0f',
			'variance': ':$,.0f',
			'variance_percent': ':.1f'
		}
	)
	
	# Customizar hover template para melhor experiência do usuário
	fig.update_traces(
		hovertemplate='<b>%{label}</b><br>' +
					 'Custo Atual: $%{value:,.0f}<br>' +
					 'Orçamento: $%{customdata[1]:,.0f}<br>' +
					 'Variação: $%{customdata[2]:,.0f}<br>' +
					 'Variação %: %{color:.1f}%<br>' +
					 '<extra></extra>',
		textinfo="label+value",
		texttemplate="<b>%{label}</b><br>$%{value:,.0f}"
	)
	
	# Configurar layout seguindo padrões dos guias
	fig.update_layout(
		title={
			'text': "📊 Mapa de Árvore - Análise de Custos vs Orçamento",
			'x': 0.5,
			'xanchor': 'center',
			'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
		},
		font=dict(family="Arial, sans-serif", size=12),
		height=700,
		paper_bgcolor='#f8f9fa',
		plot_bgcolor='white',
		coloraxis_colorbar=dict(
			title="Variação Orçamentária (%)",
			titleside="right",
			tickmode="linear",
			tick0=-10,
			dtick=5
		)
	)
	
	return dcc.Graph(figure=fig, config={'displayModeBar': True, 'toImageButtonOptions': {'format': 'png', 'filename': 'treemap_costs', 'height': 700, 'width': 1200, 'scale': 1}})

def create_detailed_table(filtered_df):
	"""Criar tabela detalhada com DataTable do Dash"""
	if filtered_df.empty:
		return html.Div("📊 Nenhum dado disponível para os filtros selecionados", 
					   style={'textAlign': 'center', 'padding': '50px', 'color': '#7f8c8d'})
	
	# Preparar dados para tabela
	table_df = filtered_df[['pillar', 'area', 'service', 'task', 'sub_task', 
						   'cost', 'budgeted_cost', 'variance', 'variance_percent', 'status']].copy()
	
	# Formatar colunas monetárias
	for col in ['cost', 'budgeted_cost', 'variance']:
		table_df[col] = table_df[col].apply(lambda x: f"${x:,.0f}")
	
	table_df['variance_percent'] = table_df['variance_percent'].apply(lambda x: f"{x:.1f}%")
	
	return html.Div([
		html.H3("📋 Tabela Detalhada de Custos", 
			   style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '20px'}),
		dash_table.DataTable(
			data=table_df.to_dict('records'),
			columns=[
				{"name": "Pilar", "id": "pillar", "type": "text"},
				{"name": "Área", "id": "area", "type": "text"},
				{"name": "Serviço", "id": "service", "type": "text"},
				{"name": "Tarefa", "id": "task", "type": "text"},
				{"name": "Sub-tarefa", "id": "sub_task", "type": "text"},
				{"name": "Custo Atual", "id": "cost", "type": "text"},
				{"name": "Orçamento", "id": "budgeted_cost", "type": "text"},
				{"name": "Variação", "id": "variance", "type": "text"},
				{"name": "Variação %", "id": "variance_percent", "type": "text"},
				{"name": "Status", "id": "status", "type": "text"}
			],
			style_cell={
				'textAlign': 'left',
				'padding': '10px',
				'fontFamily': 'Arial, sans-serif',
				'fontSize': '12px'
			},
			style_header={
				'backgroundColor': '#3498db',
				'color': 'white',
				'fontWeight': 'bold'
			},
			style_data_conditional=[
				{
					'if': {'filter_query': '{status} eq "Over Budget"'},
					'backgroundColor': '#ffebee',
					'color': 'black',
				},
				{
					'if': {'filter_query': '{status} eq "Under Budget"'},
					'backgroundColor': '#e8f5e8',
					'color': 'black',
				}
			],
			page_size=15,
			sort_action='native',
			filter_action='native'
		)
	])

def create_financial_dashboard(filtered_df):
	"""Criar dashboard financeiro com múltiplos gráficos"""
	if filtered_df.empty:
		return html.Div("📊 Nenhum dado disponível para análise financeira", 
					   style={'textAlign': 'center', 'padding': '50px', 'color': '#7f8c8d'})
	
	# Criar subplots para múltiplos gráficos
	fig = make_subplots(
		rows=2, cols=2,
		subplot_titles=('Distribuição de Custos por Pilar', 'Status do Orçamento', 
					   'Top 10 Maiores Custos', 'Análise de Variação'),
		specs=[[{"type": "pie"}, {"type": "bar"}],
			   [{"type": "bar"}, {"type": "scatter"}]]
	)
	
	# 1. Gráfico de pizza - Distribuição por pilar
	pillar_costs = filtered_df.groupby('pillar')['cost'].sum().reset_index()
	fig.add_trace(
		go.Pie(
			labels=pillar_costs['pillar'], 
			values=pillar_costs['cost'],
			name="Custos por Pilar",
			marker_colors=[pillar_colors.get(p, '#95a5a6') for p in pillar_costs['pillar']]
		),
		row=1, col=1
	)
	
	# 2. Gráfico de barras - Status do orçamento
	status_counts = filtered_df['status'].value_counts()
	status_colors = {'Over Budget': '#e74c3c', 'Under Budget': '#27ae60', 'On Budget': '#f39c12'}
	fig.add_trace(
		go.Bar(
			x=status_counts.index,
			y=status_counts.values,
			name="Status do Orçamento",
			marker_color=[status_colors.get(s, '#95a5a6') for s in status_counts.index]
		),
		row=1, col=2
	)
	
	# 3. Top 10 maiores custos
	top_costs = filtered_df.nlargest(10, 'cost')
	fig.add_trace(
		go.Bar(
			x=top_costs['cost'],
			y=top_costs['sub_task'],
			orientation='h',
			name="Top 10 Custos",
			marker_color='#3498db'
		),
		row=2, col=1
	)
	
	# 4. Scatter plot - Custo vs Orçamento
	fig.add_trace(
		go.Scatter(
			x=filtered_df['budgeted_cost'],
			y=filtered_df['cost'],
			mode='markers',
			name="Custo vs Orçamento",
			marker=dict(
				size=8,
				color=filtered_df['variance_percent'],
				colorscale='RdYlGn_r',
				showscale=True,
				colorbar=dict(title="Variação %", x=1.1)
			),
			text=filtered_df['sub_task'],
			hovertemplate='<b>%{text}</b><br>Orçamento: $%{x:,.0f}<br>Custo Real: $%{y:,.0f}<extra></extra>'
		),
		row=2, col=2
	)
	
	# Linha de referência (custo = orçamento)
	max_val = max(filtered_df['cost'].max(), filtered_df['budgeted_cost'].max())
	fig.add_trace(
		go.Scatter(
			x=[0, max_val],
			y=[0, max_val],
			mode='lines',
			name="Linha de Referência",
			line=dict(dash='dash', color='gray'),
			showlegend=False
		),
		row=2, col=2
	)
	
	# Configurar layout
	fig.update_layout(
		title_text="📈 Dashboard Financeiro Completo",
		title_x=0.5,
		height=800,
		showlegend=False,
		paper_bgcolor='#f8f9fa'
	)
	
	# Configurar eixos específicos
	fig.update_xaxes(title_text="Orçamento ($)", row=2, col=2)
	fig.update_yaxes(title_text="Custo Real ($)", row=2, col=2)
	fig.update_xaxes(title_text="Custo ($)", row=2, col=1)
	fig.update_yaxes(title_text="Quantidade", row=1, col=2)
	
	return dcc.Graph(figure=fig, config={'displayModeBar': True})

def create_variance_chart():
	"""Criar gráfico de barras de variação por pilar"""
	variance_by_pillar = df_budget.groupby('pillar').agg({
		'cost': 'sum',
		'budgeted_cost': 'sum',
		'variance': 'sum'
	}).reset_index()
	
	variance_by_pillar['variance_percent'] = (variance_by_pillar['variance'] / 
											variance_by_pillar['budgeted_cost']) * 100
	
	fig = go.Figure()
	
	# Barras de custo atual
	fig.add_trace(go.Bar(
		name='Custo Atual',
		x=variance_by_pillar['pillar'],
		y=variance_by_pillar['cost'],
		marker_color='#3498db',
		hovertemplate='Pilar: %{x}<br>Custo Atual: $%{y:,.0f}<extra></extra>'
	))
	
	# Barras de orçamento
	fig.add_trace(go.Bar(
		name='Orçamento',
		x=variance_by_pillar['pillar'],
		y=variance_by_pillar['budgeted_cost'],
		marker_color='#27ae60',
		hovertemplate='Pilar: %{x}<br>Orçamento: $%{y:,.0f}<extra></extra>'
	))
	
	fig.update_layout(
		title={
			'text': "💰 Comparação: Custo Atual vs Orçamento por Pilar",
			'x': 0.5,
			'xanchor': 'center'
		},
		xaxis_title="Pilares do Projeto",
		yaxis_title="Valor ($)",
		barmode='group',
		font=dict(family="Arial, sans-serif", size=12),
		height=400,
		yaxis_tickformat='$,.0f'
	)
	return fig

def create_variance_chart_filtered(filtered_df):
	"""Criar gráfico de barras de variação com dados filtrados"""
	if filtered_df.empty:
		return go.Figure().add_annotation(
			text="📊 Nenhum dado disponível para os filtros selecionados",
			xref="paper", yref="paper",
			x=0.5, y=0.5, xanchor='center', yanchor='middle',
			showarrow=False, font=dict(size=16, color='#7f8c8d')
		)
	
	variance_by_pillar = filtered_df.groupby('pillar').agg({
		'cost': 'sum',
		'budgeted_cost': 'sum',
		'variance': 'sum'
	}).reset_index()
	
	variance_by_pillar['variance_percent'] = (variance_by_pillar['variance'] / 
											variance_by_pillar['budgeted_cost']) * 100
	
	fig = go.Figure()
	
	# Barras de custo atual
	fig.add_trace(go.Bar(
		name='Custo Atual',
		x=variance_by_pillar['pillar'],
		y=variance_by_pillar['cost'],
		marker_color='#3498db',
		hovertemplate='Pilar: %{x}<br>Custo Atual: $%{y:,.0f}<extra></extra>'
	))
	
	# Barras de orçamento
	fig.add_trace(go.Bar(
		name='Orçamento',
		x=variance_by_pillar['pillar'],
		y=variance_by_pillar['budgeted_cost'],
		marker_color='#27ae60',
		hovertemplate='Pilar: %{x}<br>Orçamento: $%{y:,.0f}<extra></extra>'
	))
	
	fig.update_layout(
		title={
			'text': "💰 Comparação: Custo Atual vs Orçamento por Pilar (Filtrado)",
			'x': 0.5,
			'xanchor': 'center'
		},
		xaxis_title="Pilares do Projeto",
		yaxis_title="Valor ($)",
		barmode='group',
		font=dict(family="Arial, sans-serif", size=12),
		height=400,
		yaxis_tickformat='$,.0f'
	)
	return fig

# Callback para atualizar o conteúdo das abas (aba Sunburst, Barras, Treemap, Tabela)
@app.callback(
	Output('tab-content', 'children'),
	Input('visualization-tabs', 'value'),
	Input('metric-dropdown', 'value'),
	Input('pillar-filter', 'value'),
	Input('depth-slider', 'value')
)
def update_tab_content(active_tab, selected_metric, pillar_filter, depth_level):
	"""Atualiza o conteúdo das abas baseado nas seleções do usuário."""
	try:
		# Filtrar dados conforme seleção
		filtered_hierarchy = hierarchy_df.copy()
		filtered_df = df_budget.copy()

		if pillar_filter != 'all':
			filtered_hierarchy = filtered_hierarchy[
				(filtered_hierarchy['ids'].str.startswith(pillar_filter)) |
				(filtered_hierarchy['ids'] == pillar_filter)
			]
			filtered_df = filtered_df[filtered_df['pillar'] == pillar_filter]

		filtered_hierarchy = filtered_hierarchy[filtered_hierarchy['level'] <= depth_level]

		if active_tab == 'sunburst-tab':
			return create_enhanced_sunburst(filtered_df)
		elif active_tab == 'bar-tab':
			# Usar dados filtrados para o gráfico de barras
			return dcc.Graph(figure=create_variance_chart_filtered(filtered_df), style={'height': '500px'})
		elif active_tab == 'treemap-tab':
			return create_enhanced_treemap(filtered_df)
		elif active_tab == 'table-tab':
			return create_detailed_table(filtered_df)
	except Exception as e:
		return html.Div([
			html.H3("Erro ao renderizar o gráfico/tab"),
			html.Pre(str(e), style={"color": "red", "whiteSpace": "pre-wrap"})
		], style={"padding": "40px", "textAlign": "center"})


total_cost = df_budget['cost'].sum()
total_budget = df_budget['budgeted_cost'].sum()
total_variance = total_cost - total_budget

# Execução do aplicativo
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8051)



# -*- coding: utf-8 -*-

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Simulação de dados jurídicos hierárquicos
# Hierarquia: Tipo de Caso -> Área de Atuação -> Serviço -> Tarefa -> Sub-tarefa
data = [
    # Contencioso Cível
    {'tipo_caso': 'Contencioso', 'area_atuacao': 'Cível', 'servico': 'Petição Inicial', 'tarefa': 'Análise de Documentos', 'sub_tarefa': 'Análise de Provas', 'honorarios': 15000, 'horas_estimadas': 20},
    {'tipo_caso': 'Contencioso', 'area_atuacao': 'Cível', 'servico': 'Petição Inicial', 'tarefa': 'Pesquisa de Jurisprudência', 'sub_tarefa': 'Estudo de Doutrina', 'honorarios': 10000, 'horas_estimadas': 15},
    {'tipo_caso': 'Contencioso', 'area_atuacao': 'Cível', 'servico': 'Contestação', 'tarefa': 'Redação da Peça', 'sub_tarefa': 'Elaboração da Tese', 'honorarios': 20000, 'horas_estimadas': 25},

    # Contencioso Trabalhista
    {'tipo_caso': 'Contencioso', 'area_atuacao': 'Trabalhista', 'servico': 'Recurso Ordinário', 'tarefa': 'Análise do Processo', 'sub_tarefa': 'Verificação de Prazos', 'honorarios': 25000, 'horas_estimadas': 30},
    {'tipo_caso': 'Contencioso', 'area_atuacao': 'Trabalhista', 'servico': 'Recurso Ordinário', 'tarefa': 'Redação do Recurso', 'sub_tarefa': 'Fundamentação Jurídica', 'honorarios': 35000, 'horas_estimadas': 40},

    # Consultivo Tributário
    {'tipo_caso': 'Consultivo', 'area_atuacao': 'Tributário', 'servico': 'Parecer Jurídico', 'tarefa': 'Análise da Legislação', 'sub_tarefa': 'Estudo de Caso', 'honorarios': 40000, 'horas_estimadas': 50},
    {'tipo_caso': 'Consultivo', 'area_atuacao': 'Tributário', 'servico': 'Planejamento Tributário', 'tarefa': 'Reunião com Cliente', 'sub_tarefa': 'Alinhamento Estratégico', 'honorarios': 50000, 'horas_estimadas': 60},

    # Consultivo Contratual
    {'tipo_caso': 'Consultivo', 'area_atuacao': 'Contratual', 'servico': 'Elaboração de Contrato', 'tarefa': 'Definição de Cláusulas', 'sub_tarefa': 'Negociação com a Outra Parte', 'honorarios': 30000, 'horas_estimadas': 35},
    {'tipo_caso': 'Consultivo', 'area_atuacao': 'Contratual', 'servico': 'Revisão de Contrato', 'tarefa': 'Análise de Riscos', 'sub_tarefa': 'Sugestão de Alterações', 'honorarios': 22000, 'horas_estimadas': 28},
]
df_juridico = pd.DataFrame(data)

app = Dash(__name__)

# Obter valores mínimos e máximos de honorários para o RangeSlider
min_honorarios = df_juridico['honorarios'].min()
max_honorarios = df_juridico['honorarios'].max()

# Layout do Dashboard Jurídico
app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif'}, children=[
    html.H1("Painel Jurídico: Análise de Custos e Casos", style={'textAlign': 'center', 'color': '#1a2c5b'}),

    html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'}, children=[
        html.Div(style={'width': '30%'}, children=[
            html.Label("Selecione o Tipo de Caso:"),
            dcc.Dropdown(
                id='tipo-caso-dropdown',
                options=[{'label': i, 'value': i} for i in df_juridico['tipo_caso'].unique()] + [{'label': 'Todos', 'value': 'Todos'}],
                value='Todos'
            ),
        ]),
        html.Div(style={'width': '30%'}, children=[
            html.Label("Selecione a Área de Atuação:"),
            dcc.Dropdown(
                id='area-atuacao-dropdown',
                value='Todos'
            ),
        ]),
        html.Div(style={'width': '30%'}, children=[
            html.Label("Selecione o Serviço:"),
            dcc.Dropdown(
                id='servico-dropdown',
                value='Todos'
            ),
        ]),
    ]),

    html.Div(style={'padding': '0 40px'}, children=[
        html.Label("Filtrar por Faixa de Honorários:"),
        dcc.RangeSlider(
            id='honorarios-range-slider',
            min=min_honorarios,
            max=max_honorarios,
            value=[min_honorarios, max_honorarios],
            marks={int(min_honorarios): f'R${int(min_honorarios):,}', int(max_honorarios): f'R${int(max_honorarios):,}'},
            step=5000
        ),
    ]),

    dcc.Graph(id='sunburst-chart-juridico')
])

# Callback para atualizar o gráfico e os dropdowns dinamicamente
@app.callback(
    Output('sunburst-chart-juridico', 'figure'),
    Output('area-atuacao-dropdown', 'options'),
    Output('servico-dropdown', 'options'),
    Input('tipo-caso-dropdown', 'value'),
    Input('area-atuacao-dropdown', 'value'),
    Input('servico-dropdown', 'value'),
    Input('honorarios-range-slider', 'value')
)
def update_juridical_dashboard(selected_tipo_caso, selected_area, selected_servico, honorarios_range):
    filtered_df = df_juridico.copy()

    # Lógica para atualizar dropdowns em cascata
    area_options_df = filtered_df
    if selected_tipo_caso != 'Todos':
        area_options_df = filtered_df[filtered_df['tipo_caso'] == selected_tipo_caso]

    servico_options_df = area_options_df
    if selected_area != 'Todos' and selected_area is not None:
        servico_options_df = area_options_df[area_options_df['area_atuacao'] == selected_area]

    area_options = [{'label': i, 'value': i} for i in area_options_df['area_atuacao'].unique()] + [{'label': 'Todos', 'value': 'Todos'}]
    servico_options = [{'label': i, 'value': i} for i in servico_options_df['servico'].unique()] + [{'label': 'Todos', 'value': 'Todos'}]

    # Filtragem do DataFrame principal para o gráfico
    if selected_tipo_caso != 'Todos':
        filtered_df = filtered_df[filtered_df['tipo_caso'] == selected_tipo_caso]
    if selected_area != 'Todos' and selected_area is not None:
        filtered_df = filtered_df[filtered_df['area_atuacao'] == selected_area]
    if selected_servico != 'Todos' and selected_servico is not None:
        filtered_df = filtered_df[filtered_df['servico'] == selected_servico]

    filtered_df = filtered_df[(filtered_df['honorarios'] >= honorarios_range[0]) & (filtered_df['honorarios'] <= honorarios_range[1])]

    # Mapa de cores para os tipos de caso
    custom_color_map = {
        'Contencioso': '#d62728',  # Vermelho
        'Consultivo': '#1f77b4',   # Azul
        '(?)': '#cccccc'
    }

    # Geração do gráfico Sunburst
    fig = px.sunburst(
        filtered_df,
        path=['tipo_caso', 'area_atuacao', 'servico', 'tarefa', 'sub_tarefa'],
        values='honorarios',
        color='tipo_caso',
        color_discrete_map=custom_color_map,
        custom_data=['honorarios', 'horas_estimadas']
    )

    # Configurações de layout e aparência do gráfico
    fig.update_traces(
        textinfo='label+percent parent',
        hovertemplate='<b>%{label}</b><br><br>' +
                      '<b>Honorários:</b> R$ %{customdata[0]:,.2f}<br>' +
                      '<b>Horas Estimadas:</b> %{customdata[1]}h<br>' +
                      '<b>Custo por Hora:</b> R$ %{customdata[0]/customdata[1]:,.2f}/h<br>' +
                      '<extra></extra>',
        insidetextorientation='radial',
        textfont_size=12,
        marker=dict(line=dict(color='#ffffff', width=2))
    )

    fig.update_layout(
        title_text='<b>Distribuição de Honorários por Tipo de Caso e Área de Atuação</b>',
        title_x=0.5,
        font=dict(family='Arial, sans-serif', size=14, color='black'),
        margin=dict(t=80, l=40, r=40, b=40)
    )

    return fig, area_options, servico_options

# Executar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True, port=8054)
#!/usr/bin/env python3
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Teste Dash Simples"),
    html.P("Se você está vendo isso, o Dash está funcionando!"),
    dcc.Graph(
        figure=px.bar(x=['A', 'B', 'C'], y=[1, 2, 3], title="Gráfico de Teste")
    )
])

if __name__ == '__main__':
    print("Iniciando servidor Dash...")
    print("Acesse: http://localhost:8051")
    app.run_server(debug=True, port=8051, host='0.0.0.0')

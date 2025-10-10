#!/usr/bin/env python3
"""A minimal Dash application for testing the environment.

This script creates a very basic, standalone Dash application with a
single header, paragraph, and a simple bar chart. Its primary purpose is
to verify that the Dash and Plotly libraries are installed and working
correctly in the execution environment.
"""
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)
# A simple Dash application instance for testing the environment.

app.layout = html.Div([
    # The main container for the test app's layout.
    # A simple header for the test page.
    html.H1("Teste Dash Simples"),
    # A paragraph indicating that the app is running.
    html.P("Se você está vendo isso, o Dash está funcionando!"),
    # A simple bar chart to test Plotly integration.
    dcc.Graph(
        figure=px.bar(x=['A', 'B', 'C'], y=[1, 2, 3], title="Gráfico de Teste")
    )
])

if __name__ == '__main__':
    print("Iniciando servidor Dash...")
    print("Acesse: http://localhost:8051")
    app.run_server(debug=True, port=8051, host='0.0.0.0')

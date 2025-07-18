"""
Tema 2: Visualizações de Análise Financeira
Exemplo de gráficos para análise de dados financeiros usando Plotly
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def gerar_dados_financeiros():
    """Gera dados fictícios financeiros para demonstração"""
    np.random.seed(123)
    
    # Gerar datas para o último ano
    start_date = datetime.now() - timedelta(days=365)
    dates = [start_date + timedelta(days=x) for x in range(365)]
    
    # Simular preços de ações
    price_start = 100
    prices = [price_start]
    
    for i in range(1, 365):
        change = np.random.normal(0, 2)  # Mudança diária com média 0 e desvio 2
        new_price = max(prices[-1] + change, 10)  # Preço mínimo de 10
        prices.append(new_price)
    
    # Gerar volume de negociação
    volumes = np.random.randint(10000, 100000, 365)
    
    # Criar DataFrame
    df = pd.DataFrame({
        'Data': dates,
        'Preço': prices,
        'Volume': volumes,
        'Retorno': [0] + [((prices[i] - prices[i-1]) / prices[i-1]) * 100 for i in range(1, 365)]
    })
    
    return df

def gerar_dados_portfolio():
    """Gera dados de portfolio para demonstração"""
    ativos = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'META', 'NVDA', 'NFLX']
    
    portfolio = []
    for ativo in ativos:
        portfolio.append({
            'Ativo': ativo,
            'Quantidade': np.random.randint(10, 100),
            'Preço_Atual': np.random.uniform(50, 300),
            'Preço_Compra': np.random.uniform(40, 250),
            'Setor': np.random.choice(['Tecnologia', 'Consumo', 'Financeiro', 'Saúde'])
        })
    
    df = pd.DataFrame(portfolio)
    df['Valor_Total'] = df['Quantidade'] * df['Preço_Atual']
    df['Ganho_Perda'] = (df['Preço_Atual'] - df['Preço_Compra']) * df['Quantidade']
    df['Percentual_GP'] = ((df['Preço_Atual'] - df['Preço_Compra']) / df['Preço_Compra']) * 100
    
    return df

def criar_grafico_candlestick(df):
    """Cria gráfico de candlestick (simplificado como linha com preços)"""
    # Agrupar dados por semana para criar OHLC
    df['Semana'] = df['Data'].dt.to_period('W')
    df_week = df.groupby('Semana').agg({
        'Preço': ['first', 'max', 'min', 'last'],
        'Volume': 'sum'
    }).reset_index()
    
    df_week.columns = ['Semana', 'Open', 'High', 'Low', 'Close', 'Volume']
    df_week['Semana'] = df_week['Semana'].astype(str)
    
    fig = go.Figure(data=go.Candlestick(
        x=df_week['Semana'],
        open=df_week['Open'],
        high=df_week['High'],
        low=df_week['Low'],
        close=df_week['Close'],
        name="Preço Semanal"
    ))
    
    fig.update_layout(
        title='Gráfico de Candlestick - Evolução Semanal do Preço',
        yaxis_title='Preço (R$)',
        xaxis_title='Semana',
        font=dict(size=12),
        title_x=0.5,
        xaxis_rangeslider_visible=False
    )
    
    return fig

def criar_dashboard_portfolio(df_portfolio):
    """Cria dashboard com múltiplos gráficos do portfolio"""
    # Criar subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Distribuição por Valor', 'Ganho/Perda por Ativo', 
                       'Distribuição por Setor', 'Performance (%)'),
        specs=[[{"type": "pie"}, {"type": "bar"}],
               [{"type": "pie"}, {"type": "bar"}]]
    )
    
    # Gráfico de pizza - Distribuição por valor
    fig.add_trace(
        go.Pie(labels=df_portfolio['Ativo'], values=df_portfolio['Valor_Total'],
               name="Valor Total"),
        row=1, col=1
    )
    
    # Gráfico de barras - Ganho/Perda
    colors = ['green' if x > 0 else 'red' for x in df_portfolio['Ganho_Perda']]
    fig.add_trace(
        go.Bar(x=df_portfolio['Ativo'], y=df_portfolio['Ganho_Perda'],
               marker_color=colors, name="Ganho/Perda"),
        row=1, col=2
    )
    
    # Gráfico de pizza - Distribuição por setor
    setor_dist = df_portfolio.groupby('Setor')['Valor_Total'].sum().reset_index()
    fig.add_trace(
        go.Pie(labels=setor_dist['Setor'], values=setor_dist['Valor_Total'],
               name="Por Setor"),
        row=2, col=1
    )
    
    # Gráfico de barras - Performance percentual
    colors_perf = ['green' if x > 0 else 'red' for x in df_portfolio['Percentual_GP']]
    fig.add_trace(
        go.Bar(x=df_portfolio['Ativo'], y=df_portfolio['Percentual_GP'],
               marker_color=colors_perf, name="Performance %"),
        row=2, col=2
    )
    
    fig.update_layout(
        title_text="Dashboard de Portfolio - Análise Financeira",
        title_x=0.5,
        showlegend=False,
        height=700
    )
    
    return fig

def criar_grafico_retornos(df):
    """Cria gráfico de distribuição de retornos"""
    fig = go.Figure()
    
    # Histograma de retornos
    fig.add_trace(go.Histogram(
        x=df['Retorno'],
        nbinsx=50,
        name="Distribuição de Retornos",
        marker_color='lightblue',
        opacity=0.7
    ))
    
    fig.update_layout(
        title='Distribuição de Retornos Diários',
        xaxis_title='Retorno (%)',
        yaxis_title='Frequência',
        font=dict(size=12),
        title_x=0.5
    )
    
    return fig

def main():
    """Função principal para gerar e exibir os gráficos financeiros"""
    print("Gerando dados financeiros...")
    
    # Gerar dados
    df_precos = gerar_dados_financeiros()
    df_portfolio = gerar_dados_portfolio()
    
    print("Dados gerados:")
    print("Dados de preços:", len(df_precos), "registros")
    print("Portfolio:", len(df_portfolio), "ativos")
    print("\nPortfolio:")
    print(df_portfolio[['Ativo', 'Valor_Total', 'Ganho_Perda', 'Percentual_GP']].round(2))
    
    # Criar gráficos
    print("\nCriando gráficos...")
    fig1 = criar_grafico_candlestick(df_precos)
    fig2 = criar_dashboard_portfolio(df_portfolio)
    fig3 = criar_grafico_retornos(df_precos)
    
    # Exibir gráficos
    print("Exibindo gráficos...")
    fig1.show()
    fig2.show()
    fig3.show()
    
    # Salvar gráficos como HTML
    print("\nSalvando gráficos como HTML...")
    fig1.write_html("tema2_candlestick.html")
    fig2.write_html("tema2_dashboard_portfolio.html")
    fig3.write_html("tema2_distribuicao_retornos.html")
    
    print("Gráficos financeiros salvos com sucesso!")

if __name__ == "__main__":
    main()
"""
Tema 1: Visualizações de Análise de Vendas
Exemplo de gráficos para análise de dados de vendas usando Plotly
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def gerar_dados_vendas():
    """Gera dados fictícios de vendas para demonstração"""
    np.random.seed(42)
    
    # Dados mensais de vendas
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
             'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
    
    dados = []
    for produto in produtos:
        vendas = np.random.randint(50, 200, 12)
        for i, mes in enumerate(meses):
            dados.append({
                'Mês': mes,
                'Produto': produto,
                'Vendas': vendas[i],
                'Receita': vendas[i] * np.random.uniform(10, 50)
            })
    
    return pd.DataFrame(dados)

def criar_grafico_barras_agrupadas(df):
    """Cria gráfico de barras agrupadas por produto e mês"""
    fig = px.bar(df, x='Mês', y='Vendas', color='Produto',
                 title='Vendas Mensais por Produto',
                 labels={'Vendas': 'Quantidade Vendida', 'Mês': 'Mês do Ano'},
                 color_discrete_sequence=px.colors.qualitative.Set2)
    
    fig.update_layout(
        xaxis_title="Mês",
        yaxis_title="Quantidade Vendida",
        legend_title="Produtos",
        font=dict(size=12),
        title_x=0.5
    )
    
    return fig

def criar_grafico_linha_receita(df):
    """Cria gráfico de linhas para receita por produto"""
    df_receita = df.groupby(['Mês', 'Produto'])['Receita'].sum().reset_index()
    
    fig = px.line(df_receita, x='Mês', y='Receita', color='Produto',
                  title='Evolução da Receita por Produto',
                  markers=True,
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    
    fig.update_layout(
        xaxis_title="Mês",
        yaxis_title="Receita (R$)",
        legend_title="Produtos",
        font=dict(size=12),
        title_x=0.5
    )
    
    return fig

def criar_heatmap_vendas(df):
    """Cria heatmap de vendas por produto e mês"""
    df_pivot = df.pivot_table(values='Vendas', index='Produto', columns='Mês', aggfunc='sum')
    
    fig = go.Figure(data=go.Heatmap(
        z=df_pivot.values,
        x=df_pivot.columns,
        y=df_pivot.index,
        colorscale='Viridis',
        colorbar=dict(title="Vendas")
    ))
    
    fig.update_layout(
        title='Heatmap de Vendas por Produto e Mês',
        xaxis_title="Mês",
        yaxis_title="Produto",
        font=dict(size=12),
        title_x=0.5
    )
    
    return fig

def main():
    """Função principal para gerar e exibir os gráficos"""
    # Gerar dados
    df = gerar_dados_vendas()
    
    print("Dados de vendas gerados:")
    print(df.head())
    print(f"\nTotal de registros: {len(df)}")
    
    # Criar gráficos
    fig1 = criar_grafico_barras_agrupadas(df)
    fig2 = criar_grafico_linha_receita(df)
    fig3 = criar_heatmap_vendas(df)
    
    # Exibir gráficos
    print("\nExibindo gráficos...")
    fig1.show()
    fig2.show()
    fig3.show()
    
    # Salvar gráficos como HTML
    print("\nSalvando gráficos como HTML...")
    fig1.write_html("tema1_vendas_barras.html")
    fig2.write_html("tema1_receita_linhas.html")
    fig3.write_html("tema1_heatmap_vendas.html")
    
    print("Gráficos salvos com sucesso!")

if __name__ == "__main__":
    main()
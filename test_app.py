#!/usr/bin/env python3
"""
Script para testar o aplicativo Dash melhorado
"""
import sys
sys.path.append('/workspaces/Py_Vy_000')

try:
    from sunburst_cost_explorer_app import df_budget, pillar_colors, app
    print('✅ Aplicativo carregado com sucesso!')
    print(f'📊 Total de registros: {len(df_budget)}')
    print(f'💰 Custo total: ${df_budget["cost"].sum():,.0f}')
    print(f'🎨 Cores dos pilares: {list(pillar_colors.keys())}')
    print(f'📈 Variação total: ${(df_budget["cost"].sum() - df_budget["budgeted_cost"].sum()):,.0f}')
    print('🚀 Aplicativo pronto para ser executado!')
    
    # Testar criação de um gráfico simples
    from sunburst_cost_explorer_app import create_enhanced_sunburst
    test_viz = create_enhanced_sunburst(df_budget.head(10))
    print('✅ Função de visualização testada com sucesso!')
    
except Exception as e:
    print(f'❌ Erro: {e}')
    import traceback
    traceback.print_exc()

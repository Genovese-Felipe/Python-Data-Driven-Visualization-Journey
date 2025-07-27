
# 🚀 INSTRUÇÕES PARA EXECUTAR O APLICATIVO
# 🇧🇷 **Português** | 🇺🇸 **English**

<details>
<summary><strong>🇧🇷 Português (clique para expandir)</strong></summary>

## ✅ Status Atual
- ✅ Ambiente Python configurado em: `/workspaces/Py_Vy_000/.venv/bin/python`
- ✅ Dependências instaladas: dash, plotly, pandas, numpy
- ✅ Código verificado e sem erros de sintaxe
- ✅ Aplicativo melhorado criado seguindo os guias Plotly

## 🎯 Como Executar

### Opção 1: Aplicativo Completo (Recomendado)
```bash
cd /workspaces/Py_Vy_000
/workspaces/Py_Vy_000/.venv/bin/python sunburst_cost_explorer_app.py
```

### Opção 2: Versão Simplificada (Para Teste)
```bash
cd /workspaces/Py_Vy_000
/workspaces/Py_Vy_000/.venv/bin/python run_app.py
```

### Opção 3: Script Automatizado
```bash
cd /workspaces/Py_Vy_000
./start_app.sh
```

## 🌐 Acesso ao Aplicativo
Após executar qualquer uma das opções acima:
1. Aguarde a mensagem: "Running on http://0.0.0.0:8050"
2. Acesse: **http://localhost:8050**
3. Ou use o Simple Browser do VS Code

## 🛠️ Troubleshooting

### Se não abrir:
1. Verifique se a porta 8050 está livre:
   ```bash
   netstat -an | grep 8050
   ```

2. Mate processos anteriores:
   ```bash
   pkill -f python
   ```

3. Tente outra porta:
   - Edite o arquivo e mude `port=8050` para `port=8051`

### Logs de Debug:
- O aplicativo roda em modo debug
- Erros aparecerão no terminal
- Mudanças no código são recarregadas automaticamente

## 📊 Funcionalidades Implementadas

### ✅ Melhorias Baseadas nos Guias Plotly:

1. **Sunburst Interativo**

</details>

---

<details open>
<summary><strong>🇺🇸 English (click to expand)</strong></summary>

# 🚀 INSTRUCTIONS TO RUN THE APPLICATION

## ✅ Current Status
- ✅ Python environment configured at: `/workspaces/Py_Vy_000/.venv/bin/python`
- ✅ Dependencies installed: dash, plotly, pandas, numpy
- ✅ Code checked and free of syntax errors
- ✅ Improved app created following Plotly guides

## 🎯 How to Run

### Option 1: Full Application (Recommended)
```bash
cd /workspaces/Py_Vy_000
/workspaces/Py_Vy_000/.venv/bin/python sunburst_cost_explorer_app.py
```

### Option 2: Simplified Version (For Testing)
```bash
cd /workspaces/Py_Vy_000
/workspaces/Py_Vy_000/.venv/bin/python run_app.py
```

### Option 3: Automated Script
```bash
cd /workspaces/Py_Vy_000
./start_app.sh
```

## 🌐 Accessing the Application
After running any of the above options:
1. Wait for the message: "Running on http://0.0.0.0:8050"
2. Access: **http://localhost:8050**
3. Or use VS Code's Simple Browser

## 🛠️ Troubleshooting

### If it doesn't open:
1. Check if port 8050 is free:
   ```bash
   netstat -an | grep 8050
   ```

2. Kill previous processes:
   ```bash
   pkill -f python
   ```

3. Try another port:
   - Edit the file and change `port=8050` to `port=8051`

### Debug Logs:
- The app runs in debug mode
- Errors will appear in the terminal
- Code changes are automatically reloaded

## 📊 Implemented Features

### ✅ Improvements Based on Plotly Guides:

1. **Interactive Sunburst**

</details>
   - Hierarquia de 5 níveis (Pillar → Area → Service → Task → Sub-task)
   - Hover personalizado com informações detalhadas
   - Controle de profundidade via slider

2. **Gráficos Comparativos**
   - Barras agrupadas (Custo Real vs Orçamento)
   - Treemap com codificação de cor
   - Tabela detalhada com filtros

3. **Interface Profissional**
   - Cards de métricas KPI
   - Sistema de abas navegável
   - Filtros dinâmicos por pilar
   - Design responsivo

4. **Customizações Avançadas**
   - Paleta de cores corporativa
   - Typography consistente (Arial, sans-serif)
   - Formatação monetária adequada
   - Estados visuais para status orçamentário

## 🎨 Características Visuais

- **Cores por Status**: Verde (Under Budget), Vermelho (Over Budget), Azul (On Budget)
- **Hierarchy Colors**: Azul (Design), Laranja (Management), Verde (Construction), Vermelho (Finishing)
- **Layout**: Grid responsivo com shadows e bordas arredondadas
- **Interatividade**: Callbacks otimizados para performance

## 📈 Dados de Exemplo

O aplicativo inclui dados realistas de construção residencial:
- **Project Design**: $315,000 (Arquitetura, Engenharia, Interior)
- **Management**: $405,000 (Administração, Logística, Financeiro)
- **Construction**: $2,005,000 (Fundação, Estrutura, MEP, Acabamentos)
- **Finishing & Landscaping**: $250,000 (Móveis, Paisagismo)

**Total do Projeto**: ~$3,000,000

## 🚀 Próximos Passos

1. Execute uma das opções acima
2. Aguarde a inicialização (5-10 segundos)
3. Acesse http://localhost:8050
4. Explore as diferentes abas e filtros
5. Teste a interatividade dos gráficos

---
**Status**: ✅ Pronto para execução
**Versão**: 2.0 Advanced (Baseado nos guias Plotly XML)

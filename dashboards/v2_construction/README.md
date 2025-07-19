# 🏗️ **Dashboard V2 - Construção Avançada**

> **Dashboard sofisticado para análise de custos de construção residencial com filtros em cascata**

## 🎯 **Características**

- ✅ **Filtros em Cascata**: Pillar → Area → Service → Cost Range
- ✅ **Tooltips Detalhados**: Custo real vs. orçado + variância
- ✅ **Análise de Construção**: 4 Pillars de custos estruturados
- ✅ **Interface Profissional**: Layout limpo e intuitivo
- ✅ **Cores Personalizadas**: Cada pillar com cor única

## 🚀 **Como Executar**

```bash
cd dashboards/v2_construction/
python V2_script.py
```

**Acesse**: http://localhost:8050

## 🏗️ **Estrutura de Dados**

### **4 Pillars Principais**
1. **Project Design** 🎨
   - Architecture (Blueprint, Interior Design)
   - Engineering (Structural, MEP, Civil)

2. **Management** 📋
   - Administration (Project Mgmt, Permits, Financial)
   - Logistics (Supply Chain, Equipment Rental)

3. **Construction** 🔨
   - Site & Foundation
   - Superstructure  
   - MEP Systems
   - Interior & Exterior

4. **Finishing & Landscaping** 🌿
   - Finishing (Cabinetry, Fixtures)
   - Landscaping (Hardscaping, Softscaping)

## 🎛️ **Sistema de Filtros**

```python
# Filtros Dinâmicos
- Pillar Dropdown: 4 opções + "All"
- Area Dropdown: Atualiza baseado no Pillar
- Service Dropdown: Atualiza baseado em Pillar + Area  
- Cost Range Slider: $15,000 - $600,000
```

## 📊 **Análise Financeira**

- **Custo vs. Orçado**: Comparação em tempo real
- **Variância**: Cálculo automático de over/under budget
- **Contribuição**: Percentual do pai e do total
- **Métricas**: Hover tooltips com 5 indicadores

## 🎨 **Design System**

### **Cores por Pillar**
- **Project Design**: `#1f77b4` (Azul)
- **Management**: `#ff7f0e` (Laranja)  
- **Construction**: `#2ca02c` (Verde)
- **Finishing & Landscaping**: `#d62728` (Vermelho)

### **Tooltips Avançados**
```html
<b>Label</b>
Actual Cost: $XX,XXX
Budgeted Cost: $XX,XXX  
Variance: $X,XXX
Contribution to Parent: XX%
Contribution to Total: XX%
```

## 🔧 **Tecnologias**

- **Plotly Express**: Sunburst com cor contínua
- **Callbacks Inteligentes**: Atualização em cascata
- **Pandas**: Processamento de dados estruturados
- **Custom Data**: Integração de múltiplas métricas

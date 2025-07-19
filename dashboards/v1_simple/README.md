# 🌟 **Dashboard V1 - Sunburst Simples**

> **Dashboard básico com gráfico Sunburst hierárquico**

## 🎯 **Características**

- ✅ **Gráfico Sunburst hierárquico** com dados reais
- ✅ **Dados extraídos de HTML** funcional de referência 
- ✅ **Interface limpa** e responsiva
- ✅ **Métricas financeiras** resumidas
- ✅ **94 itens** de custo organizados hierarquicamente

## 🚀 **Como Executar**

```bash
cd dashboards/v1_simple/
python sunburst_cost_explorer_funcional.py
```

**Acesse**: http://localhost:8052

## 📊 **Estrutura de Dados**

```python
labels = ["Invoicing", "HVAC Installation", "Layout Planning", ...]
parents = ["Management/Administration/Financial Management/...", ...]
values = [310000, 85000, 175000, ...]  # Em dólares
```

## 🎨 **Recursos Visuais**

- **Sunburst Chart**: 5 níveis hierárquicos
- **Hover Tooltips**: Custo detalhado + percentual
- **Métricas Resumidas**: Custo total, número de itens, maior custo
- **Design Responsivo**: Adaptável a diferentes telas

## 💡 **Base para Evolução**

Este V1 serviu como fundação sólida para:
- V2: Adição de filtros interativos
- V3: Integração com Machine Learning

## 🔧 **Tecnologias**

- **Dash**: Framework web
- **Plotly**: Gráfico Sunburst 
- **Pandas**: Manipulação de dados
- **HTML/CSS**: Styling customizado

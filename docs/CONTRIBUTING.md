# 🤝 **CONTRIBUTING - Python Data Driven Visualization Journey**

## **Bem-vindo aos Contribuidores!** 🎉

Este projeto foi desenvolvido de forma colaborativa entre humano e IA, resultando em **3 dashboards Dash funcionais** com crescente complexidade. Contribuições são bem-vindas!

## 🎯 **Como Contribuir**

### **1. Reportar Bugs** 🐛
```markdown
**Template de Bug Report:**
- Dashboard Version: [V1/V2/V3]
- Python Version: [3.12.x]
- Dash Version: [2.16.1]
- Error Message: [Copiar traceback completo]
- Steps to Reproduce: [Passos detalhados]
- Expected vs Actual: [O que deveria vs o que aconteceu]
```

### **2. Sugerir Melhorias** 💡
```markdown
**Template de Feature Request:**
- Dashboard Target: [V1/V2/V3 ou Nova versão]
- Use Case: [Por que é necessário]
- Implementation Ideas: [Como pode ser feito]
- Alternative Solutions: [Outras abordagens]
```

### **3. Contribuir com Código** 💻

#### **Setup do Ambiente de Desenvolvimento:**
```bash
# Clone do repositório
git clone <repository-url>
cd Py_Vy_000

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt

# Testar se tudo funciona
python dashboards/v1_simple/sunburst_cost_explorer_funcional.py
```

#### **Padrões de Código:**

**✅ Boas Práticas:**
```python
# Imports organizados
import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Comentários úteis
def create_sunburst_data():
    """
    Cria dados estruturados para o sunburst chart
    Returns: list de dicts com parent-child relationships
    """
    pass

# Layout limpo e legível
app.layout = html.Div([
    html.H1("Dashboard Title", className="header"),
    dcc.Graph(id="main-graph"),
    html.Div(id="filters", children=[
        # Filtros organizados
    ])
])

# Callbacks simples e focados
@callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(selected_value):
    # Lógica clara e documentada
    return figure
```

**❌ Evitar:**
```python
# Imports bagunçados
from dash import *
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import random

# Código sem comentários
def func(x,y,z):
    return x+y*z

# Layout tudo em uma linha
app.layout = html.Div([html.H1("Title"),dcc.Graph(id="g1"),html.Div([dcc.Dropdown()])])

# Callbacks complexos demais
@callback([Output('1','f'),Output('2','f'),Output('3','f')],
          [Input('a','v'),Input('b','v'),Input('c','v')])
def mega_callback(a,b,c):
    # 100 linhas de código...
```

## 🔄 **Workflow de Desenvolvimento**

### **Branch Strategy:**
```bash
main                    # Produção - apenas código estável
├── develop            # Desenvolvimento - novas features
├── feature/v4-auth    # Features específicas
├── hotfix/v3-bug-123  # Correções urgentes
└── release/v4.0.0     # Preparação de release
```

### **Commit Convention:**
```bash
# Formato: type(scope): description

feat(v3): add ML prediction model
fix(v2): resolve dropdown cascade issue  
docs(readme): update installation instructions
refactor(v1): simplify callback structure
test(v3): add unit tests for ML module
```

### **Pull Request Process:**

1. **Fork** o repositório
2. **Criar branch** para sua feature: `git checkout -b feature/amazing-feature`
3. **Desenvolver** seguindo os padrões
4. **Testar** em todos os 3 dashboards
5. **Commit** usando convenção
6. **Push** para seu fork: `git push origin feature/amazing-feature`
7. **Abrir PR** com template:

```markdown
## 📋 **Descrição**
Breve descrição das mudanças.

## 🎯 **Tipo de Mudança**
- [ ] Bug fix (correção que resolve problema)
- [ ] New feature (nova funcionalidade)
- [ ] Breaking change (mudança que quebra compatibilidade)
- [ ] Documentation update

## 🧪 **Testes Realizados**
- [ ] V1 Dashboard funcionando
- [ ] V2 Dashboard funcionando  
- [ ] V3 Dashboard funcionando
- [ ] Testes unitários passando

## 📸 **Screenshots (se aplicável)**
[Incluir imagens das mudanças visuais]

## 📝 **Checklist**
- [ ] Código segue os padrões do projeto
- [ ] Self-review realizado
- [ ] Comentários em código complexo
- [ ] Documentação atualizada
```

## 🏗️ **Arquitetura e Extensibilidade**

### **Adicionando Nova Versão (V4+):**

1. **Criar estrutura:**
```bash
mkdir -p dashboards/v4_enterprise
touch dashboards/v4_enterprise/app.py
touch dashboards/v4_enterprise/README.md
```

2. **Template base:**
```python
# dashboards/v4_enterprise/app.py
import dash
from dash import dcc, html
import plotly.express as px

# Inicialização padrão
app = dash.Dash(__name__)

# Layout base
app.layout = html.Div([
    html.H1("V4 - Enterprise Dashboard"),
    # Seus componentes aqui
])

# Callbacks

# Execução padrão
if __name__ == '__main__':
    app.run(debug=True, port=8054)  # Nova porta
```

3. **Documentar:**
```markdown
# V4 Enterprise Dashboard

## Features
- Lista de novidades

## Usage  
python dashboards/v4_enterprise/app.py

## Dependencies
pip install additional-requirements
```

### **Modificando Versões Existentes:**

**V1 (Simples):** Ideal para:
- Correções de bugs simples
- Melhorias de UI básicas
- Otimizações de performance

**V2 (Intermediário):** Ideal para:
- Novos tipos de filtros
- Visualizações adicionais
- Melhorias de UX

**V3 (Avançado):** Ideal para:
- Novos algoritmos ML
- Visualizações complexas
- Integrações externas

## 🧪 **Testes**

### **Estrutura de Testes:**
```bash
tests/
├── test_v1_basic.py
├── test_v2_filters.py  
├── test_v3_ml.py
└── test_utils.py
```

### **Executar Testes:**
```bash
# Todos os testes
pytest

# Testes específicos
pytest tests/test_v3_ml.py

# Coverage report
pytest --cov=dashboards
```

### **Exemplo de Teste:**
```python
import pytest
from dashboards.v1_simple.sunburst_cost_explorer_funcional import app

def test_app_runs():
    """Testa se o app V1 inicializa corretamente"""
    assert app.server is not None

def test_layout_exists():
    """Testa se layout foi definido"""
    assert app.layout is not None
```

## 📚 **Recursos Adicionais**

### **Links Úteis:**
- [Dash Documentation](https://dash.plotly.com/)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Scikit-learn Guide](https://scikit-learn.org/stable/user_guide.html)

### **Comunidade:**
- **Issues**: Para reportar problemas
- **Discussions**: Para ideias e perguntas
- **Wiki**: Documentação avançada

---

## 🏆 **Contributors**

Agradecemos a todos que contribuíram para este projeto!

<!-- Contributors will be automatically added here -->

---

**Lembre-se:** Este projeto nasceu de uma colaboração entre humano e IA. Mantenha essa filosofia de cooperação e aprendizado mútuo! 🤖🤝👨‍💻

*Última atualização: Janeiro 2024*

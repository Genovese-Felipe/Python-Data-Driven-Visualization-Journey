# 🏡 **Dashboard V3 - Smart Home Complexo**

> **Dashboard avançado com Machine Learning, mapas geográficos e múltiplas visualizações para análise de instalações de casa inteligente**

## 🎯 **Características**

- ✅ **4 Visualizações Integradas**: Sunburst + Mapa + Scatter + ML
- ✅ **Machine Learning**: Análise preditiva de economia de energia
- ✅ **Mapas Geográficos**: Coordenadas reais dos EUA
- ✅ **Design Moderno**: Cards responsivos com shadows e styling
- ✅ **Filtros Inteligentes**: Região → Cidade → Tipo de Instalação

## 🚀 **Como Executar**

```bash
cd dashboards/v3_smart_home/
python Plan_V3_funcional.py
```

**Acesse**: http://localhost:8053

## 🏡 **Domínio: Smart Home Analytics**

### **3 Tipos de Instalação**
1. **Solar Panels** ☀️ - Painéis solares ($15k-$22k)
2. **Smart Thermostat** 🌡️ - Termostatos inteligentes ($6k-$9k)
3. **Security System** 🔒 - Sistemas de segurança ($12k-$14k)

### **4 Regiões dos EUA**
- **North**: Seattle, Portland
- **South**: Austin, Dallas, Houston  
- **East**: New York, Boston
- **West**: San Francisco, Los Angeles

## 📊 **4 Visualizações Principais**

### **1. 📊 Sunburst Hierárquico**
```python
path=['Region', 'City', 'Installation_Type']
values='Installation_Cost'
color='Installation_Cost' (escala Viridis)
```

### **2. 🗺️ Mapa Geográfico** 
```python
scatter_geo(
    lat='Latitude', lon='Longitude',
    size='Installation_Cost',
    color='Region',
    projection="albers usa"
)
```

### **3. 💰 Scatter Plot**
```python
x='Installation_Cost'
y='Annual_Energy_Savings' 
color='Installation_Type'
size='Customer_Satisfaction'
```

### **4. 🔮 Análise Preditiva (ML)**
```python
# Regressão Linear
features = ['Installation_Cost', 'Number_of_Devices', 'Customer_Satisfaction']
target = 'Annual_Energy_Savings'

# Gráfico de Importância das Features
Bar chart horizontal com coeficientes absolutos
```

## 🧠 **Machine Learning**

### **Modelo Preditivo**
- **Algoritmo**: Linear Regression (sklearn)
- **Target**: Economia Anual de Energia
- **Features**: 3 variáveis numéricas
- **Visualização**: Feature Importance horizontal

### **Insights Gerados**
- Qual fator mais influencia a economia?
- Relação custo-benefício por região
- Padrões geográficos de instalação

## 🎨 **Design System Avançado**

### **Layout Grid**
```css
2x2 Grid Layout:
┌─────────────┬─────────────┐
│  Sunburst   │    Mapa     │
├─────────────┼─────────────┤
│  Scatter    │  ML Chart   │
└─────────────┴─────────────┘
```

### **Styling Moderno**
- **Cards**: `backgroundColor: 'white'`
- **Shadows**: `boxShadow: '0 2px 4px rgba(0,0,0,0.1)'`
- **Border Radius**: `borderRadius: '10px'`
- **Background**: `backgroundColor: '#ecf0f1'`

### **Filtros Responsivos**
- 3 dropdowns inline (30% width each)
- Labels com `fontWeight: 'bold'`
- Margin spacing otimizado

## 🌍 **Dados Geográficos Reais**

```python
coordinates = {
    'Seattle': (47.6062, -122.3321),
    'Portland': (45.5051, -122.6750), 
    'Austin': (30.2672, -97.7431),
    'Dallas': (32.7767, -96.7970),
    # ... mais 6 cidades
}
```

## 🔧 **Tecnologias Avançadas**

- **Plotly Express**: 4 tipos de gráficos integrados
- **Scikit-Learn**: Machine Learning pipeline
- **Geo Mapping**: Coordenadas GPS reais
- **Complex Callbacks**: 1 callback → 4 outputs
- **Responsive Design**: CSS Grid + Flexbox

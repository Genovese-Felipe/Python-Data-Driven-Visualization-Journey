# 📚 **Documentação Técnica - Py_Vy_000**

## 🎯 **Arquitetura do Projeto**

### **Estrutura Técnica**
```
Py_Vy_000/
├── dashboards/           # Aplicações Dash organizadas por versão
├── docs/                 # Documentação técnica e guias 
├── error_reports/        # Análise de problemas e soluções
├── ai_learning_guides/   # Instruções para modelos de IA
├── assets/               # Recursos estáticos (HTML, imagens)
├── tema1/ & tema2/       # Código legado (manter para referência)
└── index/                # Dashboard HTML principal
```

### **Dependências Principais**
| Biblioteca | Versão | Finalidade |
|------------|---------|------------|
| `dash` | 2.16.1 | Framework web principal |
| `plotly` | 5.17.0 | Visualizações interativas |
| `pandas` | 2.1.4 | Manipulação de dados |
| `scikit-learn` | 1.3.2 | Machine Learning (V3) |

## 🚀 **Deployment**

### **Desenvolvimento Local**
```bash
python dashboards/v1_simple/sunburst_cost_explorer_funcional.py
python dashboards/v2_construction/V2_script.py  
python dashboards/v3_smart_home/Plan_V3_funcional.py
```

### **Produção (Gunicorn)**
```bash
gunicorn --bind 0.0.0.0:8080 dashboards.v3_smart_home.Plan_V3_funcional:app
```

### **Docker (Opcional)**
```dockerfile
FROM python:3.12-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8053
CMD ["python", "dashboards/v3_smart_home/Plan_V3_funcional.py"]
```

## 🔧 **Configurações de Ambiente**

### **Variáveis de Ambiente**
```bash
export DASH_DEBUG=True          # Para desenvolvimento
export DASH_HOST=0.0.0.0        # Host padrão
export DASH_PORT=8053           # Porta padrão V3
```

### **Performance**
- **Threads**: Dash usa threading automático
- **Memory**: ~100MB por dashboard ativo
- **CPU**: Baixo uso, spikes durante callbacks

## 📊 **Especificações dos Dashboards**

### **V1 - Sunburst Simples**
- **Dados**: 94 itens hierárquicos
- **Memória**: ~50MB 
- **Render Time**: ~2s primeira carga
- **Interatividade**: Hover apenas

### **V2 - Construção Avançada**  
- **Dados**: 48 registros estruturados
- **Filtros**: 4 dropdowns em cascata
- **Callbacks**: 2 principais
- **Performance**: ~3s atualização completa

### **V3 - Smart Home Complexo**
- **Visualizações**: 4 gráficos simultâneos
- **ML**: LinearRegression (10 samples)
- **Geo Data**: 10 coordenadas EUA
- **Callbacks**: 1 master callback → 4 outputs

## 🐛 **Troubleshooting**

### **Erros Comuns**
```python
# Port já em uso
OSError: [Errno 98] Address already in use
# Solução: Mudar porta ou matar processo

# Import Error  
ModuleNotFoundError: No module named 'dash'
# Solução: pip install -r requirements.txt

# Callback Error
dash.exceptions.DuplicateCallbackOutput
# Solução: IDs únicos, callbacks não conflitantes
```

### **Performance Issues**
```python
# Se dashboard está lento:
1. Reduzir tamanho dos dados
2. Simplificar callbacks
3. Usar caching se necessário
4. Verificar loops infinitos em callbacks
```

## 🔒 **Segurança**

### **Desenvolvimento**
```python
app.run(debug=True)  # Apenas para dev
```

### **Produção** 
```python
app.run(debug=False, host='127.0.0.1')  # Mais seguro
```

## 📈 **Métricas e Monitoramento**

### **KPIs dos Dashboards**
- **Tempo de Carregamento**: < 5s
- **Taxa de Erro**: 0%
- **Responsividade**: 100% mobile-friendly
- **Disponibilidade**: 99.9%

### **Logs Importantes**
```bash
# Verificar logs de erro:
tail -f /var/log/dash_app.log

# Monitorar performance:
htop  # CPU/Memory usage
netstat -tulpn | grep :8053  # Port status
```

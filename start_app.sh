echo "🚀 Iniciando Explorador de Custos de Construção..."
#!/bin/bash
# Script de inicialização do app (PT)
# App startup script (EN)
echo "🚀 Iniciando Explorador de Custos de Construção... / Starting Construction Cost Explorer..."

# Matar processos existentes na porta 8050
pkill -f "python.*app"
sleep 1

# Executar aplicativo em background
cd /workspaces/Py_Vy_000
/workspaces/Py_Vy_000/.venv/bin/python app_simples.py &

# Aguardar inicialização
sleep 5

# Verificar se está rodando
if curl -s http://localhost:8050 > /dev/null; then
    echo "✅ Aplicativo iniciado com sucesso!"
    echo "🌐 Acesse: http://localhost:8050"
    echo "📊 Interface carregada e pronta para uso"
else
    echo "❌ Erro ao iniciar aplicativo"
fi

echo "🔄 Aplicativo rodando em background..."
echo "🛑 Para parar: pkill -f python"

#!/bin/bash

# Script de desenvolvimento otimizado para MkDocs
# Inicia o servidor com fast reload habilitado

set -e

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Iniciando servidor de desenvolvimento MkDocs com fast reload...${NC}"
echo ""

# Verifica se está em ambiente virtual
if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${BLUE}⚠️  Ambiente virtual não detectado. Ativando venv...${NC}"
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
    elif [ -f "venv/bin/activate.fish" ]; then
        echo "Detectado Fish shell. Use: source venv/bin/activate.fish"
    fi
fi

# Verifica se mkdocs está instalado
if ! command -v mkdocs &> /dev/null; then
    echo -e "${BLUE}❌ MkDocs não encontrado. Instalando dependências...${NC}"
    pip install -r requirements.txt
fi

# Inicia o servidor com fast reload
echo -e "${GREEN}✅ Servidor iniciado com --dirtyreload (fast reload)${NC}"
echo -e "${GREEN}📝 Editando arquivos em docs/ para ver mudanças em tempo real${NC}"
echo ""

mkdocs serve --dirtyreload --watch-theme


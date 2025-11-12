#!/bin/bash

# Script de instalación para la calculadora web
# Uso: ./setup.sh

echo "Instalando calculadora web modular..."
echo "======================================"

# Verificar que Python esté instalado
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 no está instalado"
    exit 1
fi

echo "Python 3 encontrado: $(python3 --version)"

# Verificar que estamos en el directorio correcto
if [ ! -f "app.py" ]; then
    echo "Error: Debe ejecutar este script desde el directorio calculadora-web/"
    exit 1
fi

echo "Instalación completada. Puede ejecutar:"
echo "  python app.py"
echo "para iniciar el servidor."

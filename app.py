"""
Aplicación principal de la calculadora web.
"""
import sys
import os

# Agregar el directorio actual al path para importar el módulo calculadora
sys.path.append(os.path.dirname(__file__))

from calculadora.servidor import iniciar_servidor

def main():
    """Función principal que inicia el servidor de la calculadora."""
    print("Calculadora Web Modular")
    print("======================")
    
    # Obtener el puerto de la variable de entorno o usar el predeterminado
    puerto = int(os.environ.get('PORT', 8000))
    
    # Para PythonAnywhere, necesitamos enlazar a 0.0.0.0
    host = os.environ.get('HOST', '')
    
    try:
        iniciar_servidor(puerto=puerto, host=host)
    except Exception as e:
        print(f"Error al iniciar el servidor: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

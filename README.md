# Calculadora Web Modular

Una calculadora web implementada completamente en Python estándar, sin el uso de frameworks externos.

## Características

- **Arquitectura modular**: Código organizado en módulos separados
- **Sin frameworks**: Solo Python estándar y bibliotecas built-in
- **Pruebas unitarias**: Cobertura completa con unittest
- **Interfaz web responsive**: Funciona en desktop y móviles
- **Operaciones soportadas**:
  - Operaciones básicas: suma, resta, multiplicación, división
  - Potencias y raíces cuadradas
  - Cálculo de porcentajes
  - Evaluación de expresiones matemáticas

## Estructura del Proyecto

```
calculadora-web/
├── calculadora/          # Módulos de la calculadora
│   ├── __init__.py
│   ├── operaciones.py    # Lógica de operaciones matemáticas
│   └── servidor.py       # Servidor web HTTP
├── pruebas/              # Pruebas unitarias
│   ├── __init__.py
│   └── test_operaciones.py
├── static/               # Archivos estáticos
│   └── style.css         # Estilos CSS
├── templates/            # Plantillas HTML
│   └── index.html        # Interfaz principal
├── app.py               # Aplicación principal
└── requirements.txt     # Dependencias (vacío)
```

## Instalación y Uso

### Ejecución Local

1. Navegar al directorio del proyecto:
   ```bash
   cd calculadora-web
   ```

2. Ejecutar la aplicación:
   ```bash
   python app.py
   ```

3. Abrir en el navegador:
   ```
   http://localhost:8000
   ```

### Ejecutar Pruebas

```bash
python -m unittest pruebas/test_operaciones.py -v
```

### Despliegue en PythonAnywhere

1. Subir todos los archivos a PythonAnywhere
2. Configurar la aplicación web para usar `app.py`
3. Asegurarse de que el puerto esté configurado correctamente

## API

### Endpoints

- `GET /` - Sirve la interfaz web
- `POST /calcular` - Realiza operaciones matemáticas

### Ejemplo de uso de la API

```javascript
// Ejemplo de solicitud para calcular una expresión
const formData = new FormData();
formData.append('operacion', 'expresion');
formData.append('expresion', '2 + 3 * 4');

fetch('/calcular', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

## Tecnologías Utilizadas

- **Backend**: Python 3.x (http.server, socketserver)
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Pruebas**: unittest (framework de pruebas de Python)
- **Sin dependencias externas**

## Seguridad

- Validación de entrada en el servidor
- Sanitización de expresiones matemáticas
- Protección contra inyección de código
- Caracteres permitidos restringidos

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

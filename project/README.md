# API de Despliegue de Modelo ML con FastAPI

Este proyecto implementa una API RESTful utilizando FastAPI para el despliegue de un modelo de machine learning.

## Características

- Endpoint para predicciones en tiempo real
- Carga eficiente del modelo pre-entrenado
- Validación de datos de entrada
- Documentación automática con Swagger/OpenAPI
- Contenedorización con Docker
- Monitoreo de rendimiento

## Requisitos
- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- Dependencias específicas del modelo (scikit-learn, TensorFlow, PyTorch, etc.)

## Instalación

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```


## Uso

### Ejecutar localmente

```bash
uvicorn app.main:app --reload
```

La API estará disponible en http://localhost:8000

### Documentación

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

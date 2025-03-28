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
poetry install 
```


## Uso

### Ejecutar localmente

```bash
poetry run fastapi dev src/app.py
```

La API estará disponible en http://localhost:8000

### Documentación

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

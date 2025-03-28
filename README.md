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


## Estructura del Proyecto

La organización de archivos y directorios del proyecto es la siguiente:

```
SERVING-ML-APP/
├── .github/               # Configuración y workflows de GitHub
├── .poetry/               # Configuración de Poetry (gestor de dependencias)
├── container/             # Archivos relacionados con la contenerización
├── models/                # Modelos de machine learning
├── notebooks/             # Jupyter notebooks para análisis y experimentación
├── src/                   # Código fuente principal de la aplicación
├── .containerignore       # Archivos a ignorar en la construcción del contenedor
├── .dockerignore          # Archivos a ignorar en la construcción de Docker
├── .gitignore             # Archivos a ignorar en Git
├── poetry.lock            # Archivo de bloqueo de dependencias de Poetry
├── pyproject.toml         # Configuración del proyecto y dependencias
└── README.md              # Documentación principal del proyecto
```


## Instalación

```bash
poetry install 
```

## Uso

### Ejecutar localmente

```bash
poetry run fastapi dev src/main.py
```

La API estará disponible en http://localhost:8000

## Ejecutar en contenedor

```bash
docker build -t ml-model -f container/Containerfile .
docker run -d -p 127.0.0.1:8080:8080 ml-model
```

### Documentación

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc


# API de Despliegue de Modelo de Machine Learning con FastAPI

Este proyecto implementa una API RESTful utilizando FastAPI para el despliegue del modelo de machine learning 'multilingual-uncased-sentiment'.
Este modelo, basado en BERT, está optimizado para el análisis de sentimientos en reseñas de productos en seis idiomas: inglés, neerlandés, alemán, francés, español e italiano.
Predice la opinión de la reseña mediante un número de estrellas (entre 1 y 5).

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Dockerización](#dockerización)
- [Despliegue en Kubernetes](#despliegue-en-kubernetes)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción del Proyecto

Esta API permite a los usuarios enviar texto en uno de los seis idiomas soportados y recibir una predicción del sentimiento en forma de estrellas (1 a 5).
Utiliza FastAPI para manejar las solicitudes HTTP y el modelo 'multilingual-uncased-sentiment' para el análisis de sentimientos.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
serving-ml-app/
├── .github/
├── cloudformation/
├── container/
│   ├── Dockerfile
│   └── ...
├── data/
├── models/
├── notebooks/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── ...
│   ├── core/
│   ├── models/
│   └── ...
├── .containerignore
├── .dockerignore
├── .gitignore
├── .python-version
├── README.md
├── poetry.lock
└── pyproject.toml
```

## Instalación

Para ejecutar este proyecto localmente, sigue estos pasos:

1. Clonar el repositorio:

```bash
git clone https://github.com/ecaminero/serving-ml-app.git
cd serving-ml-app
```

2. Crear y activar un entorno virtual:

```bash
python -m venv venv

# En Windows
.\venv\Scripts\activate

# En Linux o macOS
source venv/bin/activate
```

3. Instalar las dependencias:

Este proyecto utiliza [Poetry](https://python-poetry.org/) para la gestión de dependencias:

```bash
poetry install
```

> **¿Usas Windows y ves un error como este?**
> ```
> Current Python version (3.10.10) is not allowed by the project (^3.11)
> ```
> Eso significa que tu sistema tiene otra versión de Python activa.  
> Puedes solucionarlo usando la ruta donde tengas instalado Python 3.11:
>
> ```bash
> poetry env use C:\ruta\a\python311.exe
> ```
>
> Para saber qué rutas tienes disponibles, ejecuta en la consola:
> ```bash
> where python
> ```
> Luego copia la ruta que corresponde a tu Python 3.11 e insértala en el comando anterior.

## Uso

Para iniciar la API localmente:

1. Asegúrate de estar en la raíz del proyecto (donde está el archivo `pyproject.toml`)

2. Ejecuta la aplicación con:

```bash
uvicorn src.main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

---

## Prueba de la API

> Este proyecto cuenta con **dos endpoints `/predict` diferentes**, uno para texto libre (modelo NLP) y otro para datos numéricos (modelo estructurado). A continuación se describen ambos.

---

### 🔸 API 1: Prueba del modelo de análisis de texto (NLP)

Mientras el servidor esté corriendo (`uvicorn src.main:app --reload`), no podrás escribir en esa terminal.

Abre una **nueva ventana de consola (CMD o PowerShell)** para ejecutar el siguiente comando:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{"text": "Esta es una excelente reseña de producto."}"
```

Una vez ejecutado, deberías ver una respuesta similar a:

```json
{
  "id": "0e1d8d73-1427-11f0-9ba3-bcf4d472f72c",
  "results": {
    "0.7878787878787878": 0.21212121212121213
  }
}
```

---

### 🔸 API 2: Prueba del modelo con atributos estructurados

#### 🔹 Opción 1: Desde el navegador con FastAPI Docs

1. Abre tu navegador y visita: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Haz clic en `POST /predict` y luego en **"Try it out"**
3. En el cuerpo del mensaje (`Request body`), pega este ejemplo de JSON:

```json
{
  "ABONO_OFERTADO": 53000,
  "CONSUMO_SBIF": 9603,
  "EDAD": 31,
  "SEXO_BIN": 1,
  "SCORE": 378,
  "DEUDA_PROM3": 992387,
  "PROME_UTILIZACION_3MESES": 1,
  "PROME_LINEA_CREDITO_3MESES": 594,
  "PROME_CANT_INSTITUTO_3MESES": 3,
  "SUMA_MOROSA_3MESES": 436,
  "Deuda_Char_008": 1,
  "Pago_Char_008": 0
}
```

4. Haz clic en **"Execute"**
5. La predicción aparecerá en la sección **Response body**

#### 🔹 Opción 2: Desde la terminal usando curl

```bash
curl -X POST "http://127.0.0.1:8000/predict" ^
 -H "Content-Type: application/json" ^
 -d "{{\"ABONO_OFERTADO\":53000,\"CONSUMO_SBIF\":9603,\"EDAD\":31,\"SEXO_BIN\":1,\"SCORE\":378,\"DEUDA_PROM3\":992387,\"PROME_UTILIZACION_3MESES\":1,\"PROME_LINEA_CREDITO_3MESES\":594,\"PROME_CANT_INSTITUTO_3MESES\":3,\"SUMA_MOROSA_3MESES\":436,\"Deuda_Char_008\":1,\"Pago_Char_008\":0}}"
```

Esto devolverá una respuesta JSON con la predicción del modelo.
## Dockerización

1. Construir la imagen Docker:

```bash
docker build -t serving-ml-app -f container/Dockerfile .
```

2. Ejecutar el contenedor:

```bash
docker run -p 8000:8000 serving-ml-app
```

![Arquitectura de la API](./arquitectura-api.png)
## Despliegue en Kubernetes

1. Crear los archivos de configuración de Kubernetes:

- `deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: serving-ml-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: serving-ml-app
  template:
    metadata:
      labels:
        app: serving-ml-app
    spec:
      containers:
      - name: serving-ml-app
        image: tu-usuario/serving-ml-app:latest
        ports:
        - containerPort: 8000
```

- `service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: serving-ml-app
spec:
  selector:
    app: serving-ml-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: LoadBalancer
```

2. Aplicar los archivos:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un *pull request* o issue si tienes sugerencias.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

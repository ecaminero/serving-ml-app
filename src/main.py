"""Entrypoint to invoke the FastAPI application service with."""
from src import __version__
import uuid
from src.base import HealthCheck, Inference
from src.model import ClienteRenegotiatorModel
from fastapi import FastAPI, status
import pandas as pd

model = ClienteRenegotiatorModel()
app = FastAPI()

@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")

@app.get("/", tags=["check"])
async def get():
    return {
        "status": status.HTTP_200_OK,
        "version": __version__
    }


@app.post("/predict", tags=["predict"])
async def predict(inference: Inference):
    df = pd.DataFrame([inference.model_dump()])
    scaled = model.scaler.transform(df)
    probabilidad = model.model.predict_proba(scaled)[0]

    return {
        "id": uuid.uuid1(),
        "probabilidad": probabilidad.tolist(),
    }
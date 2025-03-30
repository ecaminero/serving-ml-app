"""Entrypoint to invoke the FastAPI application service with."""
from src import __version__
from src.utils import id_generator
from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI()

class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""
    status: str = "OK"
    version: int = __version__



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
        "message": id_generator(),
        "status": status.HTTP_200_OK,
        "version": __version__
    }

@app.post("/predict", tags=["predict"])
async def predict():
    return {"message": "Hello World"}
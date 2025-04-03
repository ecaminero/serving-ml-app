from pydantic import BaseModel
from src import __version__

class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""
    status: str = "OK"
    version: int = __version__

class Inference(BaseModel):
    message: str

from pydantic import BaseModel
from src import __version__

class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""
    status: str = "OK"
    version: int = __version__

class Inference(BaseModel):
    ABONO_OFERTADO : float = 53000.0
    CONSUMO_SBIF: int =9603
    EDAD: float= 31.0
    SEXO_BIN:  float = 1.0
    SCORE:int =378
    DEUDA_PROM3: int = 992387
    PROME_UTILIZACION_3MESES: float = 1.0
    PROME_LINEA_CREDITO_3MESES: int = 594
    PROME_CANT_INSTITU_3MESES: int = 3
    SUMA_MOROSA_3MESES: int = 436
    Deuda_Char_008: int = 1
    Pago_Char_008: int =0


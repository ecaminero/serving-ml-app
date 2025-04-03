import os 
import pickle
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "cliente-renegociador.pkl") 
SCALER_PATH = os.path.join(PROJECT_ROOT, "models", "cliente-renegociador-scaler.pkl") 


class ClienteRenegotiatorModel:
    _instance = None
    _model = None
    _scaler = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClienteRenegotiatorModel, cls).__new__(cls)
            with open(MODEL_PATH, 'rb') as f:
                cls._model = pickle.load(f)

            with open(SCALER_PATH, 'rb') as f:
                cls._scaler = pickle.load(f)
                
        return cls._instance

    @property
    def model(self):
        return self._model

    @property
    def scaler(self):
        return self._scaler

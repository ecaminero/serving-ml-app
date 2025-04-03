import os 
import pickle
from pathlib import Path
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "multilingual-uncased-sentiment.pkl") 

class SentimentModel:
    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SentimentModel, cls).__new__(cls)
            
            if os.path.exists(MODEL_PATH):
                with open(MODEL_PATH, 'rb') as f:
                    config = pickle.load(f)
                print("Loading model from pickle file...")
                model = AutoModelForSequenceClassification.from_pretrained(config["model_path"])
                tokenizer = AutoTokenizer.from_pretrained(config["tokenizer_path"])
                
                # Recrear el pipeline
                cls._model = pipeline(config["task"], model=model, tokenizer=tokenizer)
            else:
                raise FileNotFoundError("Model file not found.")
                
        return cls._instance


    @property
    def model(self):
        return self._model
    
    def predict(self, texts):
        """Método para realizar predicciones"""
        if not isinstance(texts, list):
            texts = [texts]
        return self._model(texts)


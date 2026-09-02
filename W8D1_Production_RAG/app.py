from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Production ML API")


class PredictionRequest(BaseModel):
    value: float


@app.get("/")
def home():
    return {
        "message": "Production ML API is running"
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    prediction = request.value * 2

    return {
        "input": request.value,
        "prediction": prediction
    }
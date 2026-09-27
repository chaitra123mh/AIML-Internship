
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="W12D5 Production ML API",
    description="Production-oriented ML API for the W12D5 MLOps capstone",
    version="1.0.0",
)


class PredictionRequest(BaseModel):
    value: float


class PredictionResponse(BaseModel):
    input_value: float
    prediction: float


@app.get("/")
def root():
    return {
        "message": "W12D5 Production ML API is running",
        "status": "healthy",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    prediction = request.value * 2

    return {
        "input_value": request.value,
        "prediction": prediction,
    }
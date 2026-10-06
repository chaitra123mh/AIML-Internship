import joblib
import pandas as pd
import shap

from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = "models/healthbridge_baseline.pkl"
DATA_PATH = "data/aiml_healthcare_symptoms.csv"

# Load model and dataset
model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

# Get feature names
FEATURE_COLUMNS = [
    column
    for column in df.columns
    if column not in ["Patient_ID", "Diagnosis"]
]

# SHAP explainer
explainer = shap.TreeExplainer(model)

app = FastAPI(
    title="HealthBridge Disease Prediction API",
    description="AI-based disease prediction API with SHAP explanations"
)


class PredictionRequest(BaseModel):
    features: dict


@app.get("/")
def home():
    return {
        "message": "HealthBridge Disease Prediction API is running"
    }


@app.post("/predict")
def predict(request: PredictionRequest):

    input_data = request.features.copy()

    # Convert Gender
    if "Gender" in input_data:
        if input_data["Gender"] == "M":
            input_data["Gender"] = 0
        elif input_data["Gender"] == "F":
            input_data["Gender"] = 1

    # Check missing features
    missing_features = [
        feature
        for feature in FEATURE_COLUMNS
        if feature not in input_data
    ]

    if missing_features:
        return {
            "error": "Missing features",
            "missing_features": missing_features
        }

    # Create input DataFrame
    input_df = pd.DataFrame(
        [[input_data[feature] for feature in FEATURE_COLUMNS]],
        columns=FEATURE_COLUMNS
    )

    # Prediction
    prediction = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    confidence = float(max(probabilities))

    # SHAP explanation
    shap_values = explainer.shap_values(input_df)

    class_index = list(model.classes_).index(prediction)

    if isinstance(shap_values, list):
        values = shap_values[class_index][0]

    else:
        shap_array = shap_values

        if shap_array.ndim == 3:
            # SHAP format:
            # samples x features x classes
            values = shap_array[0, :, class_index]

        elif shap_array.ndim == 2:
            values = shap_array[0]

        else:
            values = shap_array

    # Create SHAP explanation
    feature_contributions = []

    for feature, value in zip(FEATURE_COLUMNS, values):

        # Convert numpy array/scalar safely
        value = float(value)

        feature_contributions.append({
            "feature": feature,
            "impact": value
        })

    # Sort by strongest impact
    feature_contributions.sort(
        key=lambda x: abs(x["impact"]),
        reverse=True
    )

    top_features = feature_contributions[:5]

    return {
        "predicted_disease": prediction,
        "confidence": confidence,
        "confidence_percentage": f"{confidence:.2%}",
        "shap_explanation": top_features,
        "message": (
            "This is an AI-generated prediction for decision support "
            "and should not replace professional medical evaluation."
        )
    }
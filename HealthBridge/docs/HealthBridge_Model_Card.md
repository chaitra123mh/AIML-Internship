# HealthBridge Disease Prediction Model Card

## 1. Model Overview

HealthBridge is an AI-based healthcare disease prediction system designed for decision-support purposes.

The system uses patient symptoms and health measurements to predict a possible disease. It provides a confidence score and SHAP-based feature explanations.

The system consists of:

- Random Forest disease prediction model
- FastAPI backend
- Streamlit user interface
- SHAP explainability
- MLflow experiment tracking

## 2. Intended Use

The model is intended for educational and decision-support purposes.

It can demonstrate how machine learning can use healthcare symptoms and measurements to generate a disease prediction and explain the important input features.

The prediction must not be used as a replacement for professional medical diagnosis or treatment.

## 3. Dataset

The provided HealthBridge healthcare dataset contains:

- 800 patient records
- 17 columns
- 15 input features
- 1 patient identifier
- 1 diagnosis target

The dataset contains 8 diagnosis classes:

- Influenza
- Hypertension
- Type2Diabetes
- Pneumonia
- Healthy
- Anaemia
- Gastroenteritis
- Migraine

Missing values were checked during preprocessing.

## 4. Features

The model uses:

- Age
- Gender
- Fever
- Cough
- Fatigue
- Breathlessness
- Chest Pain
- Nausea
- Headache
- BMI
- Systolic Blood Pressure
- Diastolic Blood Pressure
- SpO2
- Glucose
- HbA1c

## 5. Model

The primary model is a Random Forest Classifier.

Two configurations were evaluated using MLflow.

### Experiment 1

- n_estimators: 100
- max_depth: None
- min_samples_split: 2
- Accuracy: 80.00%
- Precision: 80.61%
- Recall: 80.00%
- F1-score: 79.82%

### Experiment 2

- n_estimators: 200
- max_depth: 10
- min_samples_split: 2
- Accuracy: 83.75%
- Precision: 84.13%
- Recall: 83.75%
- F1-score: 83.59%

The second configuration was selected for the core model experiments based on test accuracy.

## 6. Explainability

SHAP TreeExplainer is used to explain individual predictions.

The API returns the top five features influencing each prediction.

Example:

- Headache
- Gender
- Fever
- Cough
- Fatigue

SHAP values indicate the contribution of features to the model prediction. They should not be interpreted as medical causation.

## 7. API and Deployment

The model is served using FastAPI.

Main endpoint:

POST /predict

The Streamlit application communicates with the FastAPI backend.

The API provides:

- Predicted disease
- Confidence score
- SHAP explanation
- Medical decision-support disclaimer

## 8. Integration Testing

The FastAPI prediction endpoint was tested successfully.

Observed result:

- HTTP status: 200
- Prediction returned successfully
- Confidence returned successfully
- SHAP explanation returned successfully

## 9. Load Testing

A load test was performed using 50 concurrent requests.

Results:

- Total requests: 50
- Successful requests: 50
- Failed requests: 0
- Total time: 5.31 seconds
- Average latency: 1766.23 ms
- Maximum latency: 3692.77 ms
- Throughput: 9.41 requests/second

## 10. Bias and Fairness Considerations

Gender is included as an input feature in the current model.

The available dataset is relatively small, with 800 records, and it represents only eight diagnosis classes. A complete clinical fairness assessment across demographic groups has not been established.

Therefore, the model should not be assumed to provide equal performance across different demographic groups.

Additional validation using larger and more representative healthcare datasets is required before any real-world clinical use.

## 11. Limitations

Important limitations include:

- The current dataset contains only 8 disease classes, while the intended project requirement is 25+ diseases.
- The dataset contains only 800 records.
- The model has not undergone clinical validation.
- The model should not be used for medical diagnosis or treatment decisions.
- The reported metrics are based on the provided dataset and test split.
- Performance may differ on real-world patient data.
- A comprehensive demographic bias audit has not yet been established.
- SHAP explanations describe model behavior and do not establish medical causation.

## 12. Safety Disclaimer

This system provides AI-generated decision support only.

It is not a substitute for professional medical evaluation, diagnosis, or treatment.

## 13. Repository

GitHub repository:

https://github.com/chaitra123mh/AIML-Internship
# W11D1: MLflow Experiment Tracking — Setup & Logging

## Objective

Instrument a Scikit-learn model with MLflow to track experiments, compare hyperparameters, register the best model, and serve it for prediction.

## Technologies Used

- Python 3.12.5
- Scikit-learn 1.9.0
- Pandas 3.0.5
- MLflow 3.16.0
- Logistic Regression
- Iris Dataset

## MLflow Experiment

Experiment name:

`W11D1_Iris_Classification`

Five experiments were executed with different hyperparameters.

| Experiment | C | max_iter | Accuracy |
|---|---:|---:|---:|
| 1 | 0.1 | 100 | 0.9667 |
| 2 | 0.5 | 100 | 0.9667 |
| 3 | 1.0 | 100 | 0.9667 |
| 4 | 2.0 | 200 | 0.9667 |
| 5 | 5.0 | 300 | 1.0000 |

## Best Model

The best model achieved:

- Accuracy: 1.0000
- C: 5.0
- max_iter: 300

The model was registered in MLflow Model Registry as:

`W11D1_Iris_Best_Model`

Model Version:

`1`

## Model Serving

The registered model was served using MLflow Model Serving on port 5001.

The endpoint was tested successfully.

Test input:

`[5.1, 3.5, 1.4, 0.2]`

Prediction:

`[0]`

## Screenshots

- `mlflow_experiments.png`
- `mlflow_model-registry.png`
- `mlflow_prediction.png`
- `mlflow_model-serving.png`

## Result

MLflow experiment tracking, parameter and metric logging, model logging, experiment comparison, model registration, and model serving were successfully completed.
# W11D3: MLflow Model Serving & REST API

## Objective

Instrument an existing Scikit-learn model with MLflow, run multiple experiments, register the best model, and serve it through a REST API.

## Technologies

- Python
- Scikit-learn
- MLflow
- MLflow Model Registry
- REST API

## Experiments

Five Logistic Regression experiments were performed using different hyperparameters.

| Experiment | C | max_iter |
|---|---:|---:|
| 1 | 0.1 | 100 |
| 2 | 1.0 | 100 |
| 3 | 5.0 | 300 |
| 4 | 10.0 | 400 |
| 5 | 20.0 | 500 |

## MLflow Tracking

Each experiment logs:

- Hyperparameters
- Accuracy
- Model artifact
- Run ID

## Model Registry

The best model was registered as:

`W11D3_Iris_Model`

The registered model can be loaded using the MLflow Model Registry URI:

`models:/W11D3_Iris_Model/<version>`

## Model Serving

The registered model was served using:

```text
mlflow models serve -m "models:/W11D3_Iris_Model/<version>" -p 5003 --env-manager local
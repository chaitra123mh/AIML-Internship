# W11D2: MLflow Model Registry & Versioning

## Objective

Implement MLflow Model Registry and Versioning using a Scikit-learn Logistic Regression model.

## Technologies Used

- Python 3.12.5
- Scikit-learn
- MLflow 3.16.0
- Iris Dataset
- Logistic Regression

## Experiment

Experiment name:

`W11D2_Model_Versioning`

Five experiments were executed using different Logistic Regression hyperparameters.

| Experiment | C | max_iter |
|---|---:|---:|
| 1 | 0.1 | 100 |
| 2 | 1.0 | 100 |
| 3 | 5.0 | 300 |
| 4 | 10.0 | 400 |
| 5 | 20.0 | 500 |

The experiments were compared using accuracy.

## Model Registry

The best-performing model was registered in MLflow Model Registry as:

`W11D2_Iris_Model`

MLflow assigns a version number automatically to each registered model.

## Model Versioning

Model versions allow different versions of the same registered model to be tracked and managed.

A specific model version can be referenced using:

`models:/W11D2_Iris_Model/1`

## Model Serving

A registered model can be served using:

`mlflow models serve -m "models:/W11D2_Iris_Model/1" -p 5002 --env-manager local`

The model can then receive prediction requests through the MLflow serving endpoint.

## Result

The MLflow Model Registry and Versioning workflow was successfully implemented.

Five experiments were tracked, the best model was identified and registered, and a specific model version was prepared for serving.
import mlflow
import mlflow.sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


EXPERIMENT_NAME = "W11D2_Model_Versioning"

mlflow.set_experiment(EXPERIMENT_NAME)

data = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=0.2,
    random_state=42,
    stratify=data.target
)

experiments = [
    {"C": 0.1, "max_iter": 100},
    {"C": 1.0, "max_iter": 100},
    {"C": 5.0, "max_iter": 300},
    {"C": 10.0, "max_iter": 400},
    {"C": 20.0, "max_iter": 500},
]

results = []

print("=" * 60)
print("W11D2: MLFLOW MODEL REGISTRY & VERSIONING")
print("=" * 60)

for index, params in enumerate(experiments, start=1):

    with mlflow.start_run(run_name=f"version_experiment_{index}"):

        model = LogisticRegression(
            C=params["C"],
            max_iter=params["max_iter"],
            random_state=42
        )

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        mlflow.log_param("C", params["C"])
        mlflow.log_param("max_iter", params["max_iter"])
        mlflow.log_metric("accuracy", accuracy)

        mlflow.sklearn.log_model(
            model,
            name="model"
        )

        run_id = mlflow.active_run().info.run_id

        results.append({
            "experiment": index,
            "C": params["C"],
            "max_iter": params["max_iter"],
            "accuracy": accuracy,
            "run_id": run_id
        })

        print(f"\nExperiment {index}")
        print(f"C: {params['C']}")
        print(f"max_iter: {params['max_iter']}")
        print(f"Accuracy: {accuracy:.4f}")
        print(f"Run ID: {run_id}")


best_result = max(results, key=lambda x: x["accuracy"])

print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print(f"Best Accuracy: {best_result['accuracy']:.4f}")
print(f"Best C: {best_result['C']}")
print(f"Best max_iter: {best_result['max_iter']}")
print(f"Best Run ID: {best_result['run_id']}")

model_uri = f"runs:/{best_result['run_id']}/model"

print("\nRegistering best model...")

registered_model = mlflow.register_model(
    model_uri=model_uri,
    name="W11D2_Iris_Model"
)

print(f"Registered Model: {registered_model.name}")
print(f"Model Version: {registered_model.version}")

print("\n" + "=" * 60)
print("MODEL VERSIONING")
print("=" * 60)

print("The best model has been registered successfully.")
print(f"Current Model Version: {registered_model.version}")

print("\nModel Registry URI:")
print("models:/W11D2_Iris_Model/1")

print("\n" + "=" * 60)
print("W11D2 COMPLETED SUCCESSFULLY")
print("=" * 60)
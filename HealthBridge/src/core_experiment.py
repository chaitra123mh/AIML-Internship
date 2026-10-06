import os
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# --------------------------------------------------
# Load dataset
# --------------------------------------------------

DATA_PATH = "data/aiml_healthcare_symptoms.csv"

df = pd.read_csv(DATA_PATH)

X = df.drop(columns=["Patient_ID", "Diagnosis"])
y = df["Diagnosis"]

# Encode Gender
X["Gender"] = X["Gender"].map({
    "M": 0,
    "F": 1
})


# --------------------------------------------------
# Train-test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# MLflow setup
# --------------------------------------------------

mlflow.set_experiment("HealthBridge_Core_Model_Experiments")


experiments = [
    {
        "name": "Experiment_1",
        "n_estimators": 100,
        "max_depth": None,
        "min_samples_split": 2
    },
    {
        "name": "Experiment_2",
        "n_estimators": 200,
        "max_depth": 10,
        "min_samples_split": 2
    }
]


results = []


# --------------------------------------------------
# Run experiments
# --------------------------------------------------

for config in experiments:

    print("\n" + "=" * 60)
    print(config["name"])
    print("=" * 60)

    with mlflow.start_run(run_name=config["name"]):

        model = RandomForestClassifier(
            n_estimators=config["n_estimators"],
            max_depth=config["max_depth"],
            min_samples_split=config["min_samples_split"],
            random_state=42
        )

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0
        )
        recall = recall_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0
        )
        f1 = f1_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0
        )

        # Log parameters
        mlflow.log_param(
            "n_estimators",
            config["n_estimators"]
        )

        mlflow.log_param(
            "max_depth",
            config["max_depth"]
        )

        mlflow.log_param(
            "min_samples_split",
            config["min_samples_split"]
        )

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)

        # Log model
        mlflow.sklearn.log_model(
            model,
            name="model"
        )

        results.append({
            "name": config["name"],
            "model": model,
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        })

        print(f"Accuracy  : {accuracy:.4f}")
        print(f"Precision : {precision:.4f}")
        print(f"Recall    : {recall:.4f}")
        print(f"F1-score  : {f1:.4f}")


# --------------------------------------------------
# Select best model
# --------------------------------------------------

best_result = max(
    results,
    key=lambda x: x["accuracy"]
)

os.makedirs("models", exist_ok=True)

best_model_path = "models/healthbridge_core_model.pkl"

joblib.dump(
    best_result["model"],
    best_model_path
)


# --------------------------------------------------
# Final results
# --------------------------------------------------

print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print(f"Experiment : {best_result['name']}")
print(f"Accuracy   : {best_result['accuracy']:.4f}")
print(f"Precision  : {best_result['precision']:.4f}")
print(f"Recall     : {best_result['recall']:.4f}")
print(f"F1-score   : {best_result['f1_score']:.4f}")

print(f"\nBest model saved to:")
print(best_model_path)

print("\nMLflow experiment:")
print("HealthBridge_Core_Model_Experiments")
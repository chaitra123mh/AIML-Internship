import os
import joblib
import pandas as pd
import shap_
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split


# --------------------------------------------------
# 1. Load dataset and trained model
# --------------------------------------------------

DATA_PATH = "data/aiml_healthcare_symptoms.csv"
MODEL_PATH = "models/healthbridge_baseline.pkl"

df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# 2. Prepare features
# --------------------------------------------------

X = df.drop(columns=["Patient_ID", "Diagnosis"])
y = df["Diagnosis"]

# Convert Gender into numeric values
X["Gender"] = X["Gender"].map({"M": 0, "F": 1})


# --------------------------------------------------
# 3. Create the same test split used for evaluation
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# 4. Select one patient from test data
# --------------------------------------------------

sample_index = 0
sample = X_test.iloc[[sample_index]]

actual_disease = y_test.iloc[sample_index]

prediction = model.predict(sample)[0]
probabilities = model.predict_proba(sample)[0]

predicted_class_index = list(model.classes_).index(prediction)
confidence = probabilities[predicted_class_index]


# --------------------------------------------------
# 5. Create SHAP explainer
# --------------------------------------------------

explainer = shap.TreeExplainer(model)

explanation = explainer(sample)

shap_values = explanation.values


# --------------------------------------------------
# 6. Handle SHAP output for multiclass model
# --------------------------------------------------

if shap_values.ndim == 3:

    # Shape:
    # samples × features × classes

    selected_shap_values = shap_values[
        0,
        :,
        predicted_class_index
    ]

else:

    selected_shap_values = shap_values[0]


# --------------------------------------------------
# 7. Create feature importance table
# --------------------------------------------------

feature_names = sample.columns

shap_data = pd.DataFrame({
    "Feature": feature_names,
    "SHAP_Value": selected_shap_values
})

shap_data["Absolute_SHAP"] = shap_data["SHAP_Value"].abs()

shap_data = shap_data.sort_values(
    by="Absolute_SHAP",
    ascending=False
)

top_features = shap_data.head(5)


# --------------------------------------------------
# 8. Display results
# --------------------------------------------------

print("=" * 60)
print("HealthBridge SHAP Explainability")
print("=" * 60)

print(f"Actual Disease: {actual_disease}")
print(f"Predicted Disease: {prediction}")
print(f"Prediction Confidence: {confidence:.2%}")

print("\nTop Contributing Features:")
print("-" * 60)

for _, row in top_features.iterrows():

    direction = "increased" if row["SHAP_Value"] > 0 else "decreased"

    print(
        f"{row['Feature']}: "
        f"{row['SHAP_Value']:+.4f} "
        f"({direction} prediction influence)"
    )


# --------------------------------------------------
# 9. Create SHAP visualization
# --------------------------------------------------

os.makedirs("docs", exist_ok=True)

plot_data = top_features.sort_values(
    by="SHAP_Value"
)

plt.figure(figsize=(9, 5))

plt.barh(
    plot_data["Feature"],
    plot_data["SHAP_Value"]
)

plt.axvline(
    x=0,
    linewidth=1
)

plt.xlabel("SHAP Value")
plt.ylabel("Feature")
plt.title(
    f"SHAP Explanation - Predicted: {prediction}"
)

plt.tight_layout()

plot_path = "docs/shap_explanation.png"

plt.savefig(
    plot_path,
    dpi=150
)

plt.close()


# --------------------------------------------------
# 10. Save text evidence
# --------------------------------------------------

output_path = "output_shap.txt"

with open(output_path, "w", encoding="utf-8") as file:

    file.write("=" * 60 + "\n")
    file.write("HealthBridge SHAP Explainability\n")
    file.write("=" * 60 + "\n")

    file.write(
        f"Actual Disease: {actual_disease}\n"
    )

    file.write(
        f"Predicted Disease: {prediction}\n"
    )

    file.write(
        f"Prediction Confidence: {confidence:.2%}\n"
    )

    file.write("\nTop Contributing Features:\n")
    file.write("-" * 60 + "\n")

    for _, row in top_features.iterrows():

        direction = (
            "increased"
            if row["SHAP_Value"] > 0
            else "decreased"
        )

        file.write(
            f"{row['Feature']}: "
            f"{row['SHAP_Value']:+.4f} "
            f"({direction} prediction influence)\n"
        )

    file.write(
        f"\nSHAP visualization saved to: {plot_path}\n"
    )


print("\nSHAP explanation completed successfully.")
print(f"Visualization saved to: {plot_path}")
print(f"Text output saved to: {output_path}")
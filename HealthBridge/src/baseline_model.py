import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# Load the healthcare dataset
DATA_PATH = "data/aiml_healthcare_symptoms.csv"

df = pd.read_csv(DATA_PATH)

# Remove Patient_ID because it is only an identifier
X = df.drop(columns=["Patient_ID", "Diagnosis"])
y = df["Diagnosis"]

# Convert Gender into numerical values
X["Gender"] = X["Gender"].map({"M": 0, "F": 1})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Create the baseline Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("HealthBridge Baseline Model")
print("=" * 50)
print(f"Dataset size: {len(df)}")
print(f"Training records: {len(X_train)}")
print(f"Testing records: {len(X_test)}")
print(f"Number of diseases: {y.nunique()}")
print(f"Baseline Accuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Create models folder if it does not exist
os.makedirs("models", exist_ok=True)

# Save the trained model
model_path = "models/healthbridge_baseline.pkl"
joblib.dump(model, model_path)

print(f"\nModel saved to: {model_path}")
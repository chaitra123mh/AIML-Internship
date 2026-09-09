import mlflow
import time

# Start an MLflow experiment
mlflow.set_experiment("W9D5_Automated_Research_Report")

with mlflow.start_run():

    # Project information
    topic = "Artificial Intelligence in Healthcare"

    # Log parameters
    mlflow.log_param("topic", topic)
    mlflow.log_param("framework", "CrewAI + LangGraph")
    mlflow.log_param("model", "llama3.2:3b")

    # Simulated execution metrics
    start_time = time.time()

    # In a real system this would be the actual report generation time
    time.sleep(1)

    execution_time = time.time() - start_time

    # Log metrics
    mlflow.log_metric("execution_time_seconds", execution_time)
    mlflow.log_metric("agents_used", 3)

    # Log project status
    mlflow.set_tag("project", "Automated Research Report Agent")
    mlflow.set_tag("status", "completed")

    print("=" * 60)
    print("MLFLOW TRACKING")
    print("=" * 60)
    print(f"Topic: {topic}")
    print("Framework: CrewAI + LangGraph")
    print("Model: llama3.2:3b")
    print(f"Agents used: 3")
    print(f"Execution time: {execution_time:.2f} seconds")
    print("MLflow run completed successfully.")
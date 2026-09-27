# W12D1 MLOps Monitoring Strategy

## 1. Metrics to Monitor

### API Performance
- Request count
- Request success and failure rate
- Response latency
- HTTP 4xx and 5xx errors

### System Health
- CPU usage
- Memory usage
- Docker container restarts
- Container availability

### ML Monitoring
- Prediction distribution
- Model version
- Input data quality
- Missing or invalid values
- Data drift
- Prediction confidence

## 2. Alerts

Alerts should be triggered when:

- API error rate becomes high
- Response latency exceeds the expected limit
- Container restarts repeatedly
- CPU or memory usage remains high
- Input data contains unexpected values
- Significant data drift is detected
- Prediction confidence decreases significantly

## 3. Retraining Triggers

The model should be evaluated for retraining when:

- Data drift remains significant for a sustained period
- Model performance decreases when new labelled data becomes available
- The input data schema changes
- New representative training data becomes available
- Scheduled model evaluation identifies performance degradation

## 4. Monitoring Approach

For this internship demonstration, monitoring can be implemented using application logs, API health checks, Docker container statistics, and ML evaluation metrics.

In a production environment, these metrics can be connected to monitoring and alerting tools for dashboards and automated notifications.

## 5. Model Governance

Each deployed model should have:

- A unique model version
- Recorded training data version
- Recorded evaluation metrics
- Deployment date
- Rollback information

This helps maintain traceability and supports safe model updates.
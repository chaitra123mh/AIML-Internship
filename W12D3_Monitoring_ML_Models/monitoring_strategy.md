# W12D2 Containerising ML Apps - Monitoring Strategy

## 1. What to Track

### API Performance
- Request count
- Request success and failure rate
- Response latency
- HTTP 4xx and 5xx errors

### Container Health
- CPU usage
- Memory usage
- Container restarts
- Container availability

### ML Monitoring
- Prediction distribution
- Input data quality
- Missing or invalid values
- Data drift
- Prediction confidence
- Model version

## 2. Alerts

Alerts should be triggered when:

- API error rate becomes high
- Response latency exceeds the expected limit
- Container restarts repeatedly
- CPU or memory usage remains high
- Invalid input data is detected
- Significant data drift is detected
- Prediction confidence decreases significantly

## 3. Retraining Triggers

The model should be considered for retraining when:

- Significant data drift continues
- Model performance decreases on new labelled data
- Input data schema changes
- New representative training data becomes available
- Regular evaluation shows performance degradation

## 4. Monitoring Approach

For this demonstration, monitoring can use API health checks, application logs, Docker container statistics, and ML evaluation metrics.

In production, these metrics can be connected to monitoring dashboards and automated alerts.

## 5. Model Governance

Each model deployment should record:

- Model version
- Training data version
- Evaluation metrics
- Deployment date
- Rollback information

This provides traceability and supports safe model updates.
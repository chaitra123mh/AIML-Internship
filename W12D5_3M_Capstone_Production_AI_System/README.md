# W12D5: 3M Capstone — Production AI System

This project demonstrates an end-to-end production-oriented MLOps pipeline using the approved AI/ML 3M stack.

## Components

* FastAPI ML API
* Docker containerisation
* Automated testing with Pytest
* GitHub Actions CI workflow
* GitHub Container Registry image publishing
* Production monitoring strategy

## Practical Tasks Completed

### 1. Docker Containerisation

The ML API is containerised using Docker.

* Dockerfile created
* Docker image built successfully
* Container run locally
* `/health` endpoint verified
* `/predict` endpoint verified

### 2. CI/CD Workflow

The GitHub Actions workflow performs:

1. Linting
2. Automated testing
3. Docker image build
4. Docker image push to GitHub Container Registry

### 3. Monitoring Strategy

The monitoring strategy covers:

* API performance
* Request success and failure rates
* Response latency
* Container health
* CPU and memory usage
* ML prediction behaviour
* Data drift
* Alerts
* Retraining triggers
* Model governance

## Testing

Automated API tests were executed successfully.

* Health endpoint test: Passed
* Prediction endpoint test: Passed

## Evidence

The project includes evidence screenshots showing:

* Docker health endpoint
* Docker prediction endpoint
* Local API verification

## Final Deliverables

* Working Dockerised ML API
* GitHub Actions CI workflow
* Monitoring strategy documentation
* Test evidence
* Self-review checklist
* Git commits on the W12 branch

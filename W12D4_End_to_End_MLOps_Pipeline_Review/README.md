# W12D4: End-to-End MLOps Pipeline Review

This project demonstrates an end-to-end MLOps workflow for a containerised ML API.

## Components

* FastAPI ML API
* Docker containerisation
* Automated testing with Pytest
* GitHub Actions CI workflow
* Production monitoring strategy
* Health and prediction endpoints

## Endpoints

* `/health` - checks API health
* `/predict` - returns a sample prediction

## Docker

The ML API is containerised using Docker and can be built and run locally.

## CI Workflow

The GitHub Actions workflow performs:

1. Linting
2. Automated testing
3. Docker image build
4. Docker image push to GitHub Container Registry

## Monitoring

The monitoring strategy covers:

* API performance
* Container health
* ML behaviour
* Alerts
* Retraining triggers
* Model governance

## Evidence

* Docker health endpoint verified successfully.
* Docker prediction endpoint verified successfully.
* Local API tests passed successfully.

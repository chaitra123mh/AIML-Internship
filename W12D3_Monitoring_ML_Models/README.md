# W12D3: Monitoring ML Models in Production

This project demonstrates a containerised ML API with Docker and a CI/CD workflow.

## Components

- FastAPI ML API
- Docker containerisation
- Automated tests with Pytest
- GitHub Actions CI workflow
- Monitoring strategy
- Health and prediction endpoints

## Endpoints

- `/health` - checks API health
- `/predict` - returns a sample prediction

## Docker

The API is containerised using Docker and can be built and run locally.

## Monitoring

The monitoring strategy covers API performance, container health, ML behaviour, alerts, and retraining triggers.
## Evidence

- Docker health endpoint verified successfully.
- Docker prediction endpoint verified successfully.
- Local API tests passed successfully.
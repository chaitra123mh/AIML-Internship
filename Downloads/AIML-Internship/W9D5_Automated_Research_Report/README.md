# W9D5 — Automated Research Report Agent

## Overview

This project implements an Automated Research Report Agent using
the approved AI/ML 3M stack.

## Technologies

- CrewAI
- LangGraph
- MLflow
- Ragas
- Ollama
- Python

## Architecture

User Topic
↓
CrewAI Researcher
↓
CrewAI Report Writer
↓
CrewAI Reviewer
↓
LangGraph Workflow
↓
Final Research Report
↓
MLflow Tracking + Ragas Evaluation

## Files

- `research_agent.py` — CrewAI multi-agent research system
- `langgraph_workflow.py` — LangGraph workflow
- `mlflow_tracking.py` — MLflow experiment tracking
- `ragas_evaluation.py` — Ragas evaluation dataset
- `self_review.md` — Self-review checklist
- `output/` — Execution screenshots

## Model

The project uses the local Ollama model:

`llama3.2:3b`

## Result

The system successfully generated and reviewed an
automated research report on Artificial Intelligence in Healthcare.
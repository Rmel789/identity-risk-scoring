# identity-risk-scoring
ML-based identity risk scoring engine for AWS IAM + CloudTrail logs, with model cards and drift monitoring

# Identity Risk Scoring Engine

This project builds a predictive model to score AWS identities (users/roles) based on CloudTrail activity.

## Features
- Feature engineering from IAM & CloudTrail logs
- Logistic Regression / XGBoost scoring pipeline
- MLflow experiment tracking
- Model Cards for governance
- Drift detection and monitoring
- Dockerized API endpoint for scoring

## Structure
data/
  sample_cloudtrail/

src/
  etl.py
  feature_engineering.py
  train_model.py
  score.py

models/
  mlflow_runs/
  model_card.md

docker/
  Dockerfile

## Goals
- Detect risky IAM principals
- Support SOC analysts with identity-based threat signals

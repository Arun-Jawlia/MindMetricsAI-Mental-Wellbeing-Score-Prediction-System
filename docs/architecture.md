# MindMetrics AI Architecture

## Overview

MindMetrics AI is a full-stack machine learning application
that predicts a mental wellbeing score using lifestyle and
behavioral features.

## Architecture

Frontend
    ↓
FastAPI Backend
    ↓
Prediction Service
    ↓
Machine Learning Model
    ↓
Prediction Result

The backend also communicates with PostgreSQL
for storing users and prediction history.

## Components

### Frontend

React + TypeScript + Vite

Responsibilities:

- User interface
- Assessment form
- API communication
- Prediction visualization
- Dashboard
- Prediction history

### Backend

FastAPI

Responsibilities:

- REST API
- Request validation
- Authentication
- Prediction service
- Database communication
- Error handling

### ML

Python + Scikit-learn

Responsibilities:

- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Prediction

### Database

PostgreSQL

Responsibilities:

- Users
- Assessments
- Predictions
- Historical scores
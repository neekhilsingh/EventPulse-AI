# System Architecture

# 🚦 EventPulse-AI

> **Predict. Prepare. Prevent.**

---

# Overview

EventPulse-AI follows a modular, service-oriented architecture that combines Machine Learning, REST APIs, location intelligence, and AI-assisted operational decision support into a unified traffic incident management system.

The architecture is designed to be lightweight, scalable, and easy to extend for future real-time deployments.

---

# High-Level Architecture

```text
                           User

                             │

                             ▼

                 Streamlit Web Dashboard

                             │
                             │ REST API
                             ▼

                    FastAPI Backend Server

      ┌──────────────┬──────────────┬──────────────┐
      │              │              │              │
      ▼              ▼              ▼              ▼

 Random Forest   Recommendation   Emergency    Mappls API
 Prediction         Engine        Allocation  Reverse Geocode

      │              │              │              │
      └──────────────┴──────────────┴──────────────┘

                             │

                             ▼

                      JSON Response

                             │

                             ▼

               Interactive Dashboard Output
```

---

# Architecture Components

## 1. Streamlit Dashboard

The Streamlit application provides the user interface for interacting with the system.

Responsibilities:

* Collect incident information
* Send prediction requests
* Display prediction results
* Display AI recommendations
* Display emergency resources
* Display interactive map

---

## 2. FastAPI Backend

The FastAPI server acts as the central processing layer.

Responsibilities:

* Receive requests
* Validate input data
* Perform feature engineering
* Invoke ML model
* Generate recommendations
* Call Mappls API
* Allocate emergency resources
* Return structured JSON

---

## 3. Machine Learning Engine

Model Used:

**Random Forest Classifier**

Input Features include:

* Event Type
* Event Cause
* Vehicle Type
* Police Station
* Corridor
* Road Closure
* Peak Hour
* Weekend
* Month
* Day
* Event Category

Output:

* High Priority
* Low Priority
* Prediction Confidence

---

## 4. Feature Engineering Module

Transforms raw incident data into model-ready features.

Operations include:

* One-Hot Encoding
* Boolean Conversion
* Feature Alignment
* Missing Feature Handling

---

## 5. Recommendation Engine

The recommendation engine converts the prediction into actionable operational decisions.

Factors considered:

* Predicted Priority
* Peak Hour
* Road Closure
* Event Type
* Event Category
* Weekend

Outputs:

* Impact Score
* Impact Level
* Emergency Status
* Officers Required
* Barricades Required
* Diversion Requirement
* Estimated Clearance Time
* Operational Actions

---

## 6. Mappls Reverse Geocoding

Uses Mappls Reverse Geocoding API to convert GPS coordinates into readable addresses.

Input:

```
Latitude
Longitude
```

Output:

```
Formatted Address

City

State

Pincode
```

Example:

```
Kengeri Main Road
Ambedkar Circle
Bengaluru
Karnataka
560060
```

---

## 7. Emergency Resource Allocation

Provides suggested nearby emergency services.

Resources include:

* Police Station
* Hospital
* Fire Station

This enables quicker operational planning.

---

# Data Flow

```text
User submits incident

        │

        ▼

Streamlit Dashboard

        │

        ▼

POST /predict

        │

        ▼

Input Validation

        │

        ▼

Feature Engineering

        │

        ▼

Random Forest Prediction

        │

        ├────────────► Recommendation Engine

        │

        ├────────────► Emergency Allocation

        │

        └────────────► Mappls Reverse Geocoding

                     │

                     ▼

             Final JSON Response

                     │

                     ▼

          Streamlit Visualization
```

---

# Project Structure

```text

EventPulse-AI
├── app
│   ├── __pycache__
│   ├── emergency.py
│   ├── geocode.py
│   ├── main.py
│   ├── mappls.py
│   ├── predictor.py
│   ├── recommender.py
│   ├── schemas.py
│   └── utils.py
│
├── data
│   ├── Astram event data_anonymized.csv
│   ├── cleaned_traffic_events.csv
│   └── feature_engineered_events.csv
│
├── docs
│   ├── api_design.md
│   ├── architecture.md
│   └── mvp_features.md
│
├── frontend
│   └── app.py
│
├── models
│   ├── feature_columns.pkl
│   └── random_forest.pkl
│
├── notebook
│   ├── 01_EDA_Data_Cleaning.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Model_Development.ipynb
│   ├── 04_Model_Comparison.ipynb
│   └── 05_Recommendation_Engine.ipynb
│
├── screenshots
│   ├── AI_Recommendation.png
│   ├── Dashboard.png
│   ├── Emergency_Resource.png
│   ├── Interactive_Map.png
│   └── Prediction.png
│
├── venv
│
├── .env
├── .gitignore
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
└── test_mappls.py

```

---

# Technology Stack

| Layer                | Technology                   |
| -------------------- | ---------------------------- |
| Frontend             | Streamlit                    |
| Backend              | FastAPI                      |
| Machine Learning     | Scikit-learn                 |
| Data Processing      | Pandas                       |
| Model Storage        | Joblib                       |
| Location Services    | Mappls Reverse Geocoding API |
| Programming Language | Python                       |

---

# Design Principles

The system is designed using the following principles:

* Modular Architecture
* Separation of Concerns
* RESTful API Design
* Reusable Components
* Lightweight Deployment
* Extensible ML Pipeline

Each module performs a single responsibility, making the system easier to maintain and extend.

---

# Advantages of the Architecture

* Clean separation between frontend and backend
* Fast real-time predictions
* Easy integration with external APIs
* Scalable for cloud deployment
* Supports future real-time traffic feeds
* Independent ML and recommendation modules
* Modular codebase for easier maintenance

---

# Future Architecture Enhancements

Future versions may include:

* Live Traffic API Integration
* CCTV Video Analytics
* GPS-Based Incident Detection
* Real-Time Vehicle Tracking
* Notification Services
* Cloud Deployment
* Database Integration
* User Authentication
* Admin Dashboard
* Mobile Application Support

---

# Conclusion

EventPulse-AI adopts a modular architecture that combines Machine Learning, FastAPI, Streamlit, Mappls Reverse Geocoding, and an AI-driven recommendation engine into a unified intelligent traffic incident management platform. This design enables rapid predictions, operational recommendations, and efficient emergency resource allocation while remaining scalable for future smart-city deployments.

# 🚦 EventPulse-AI

> **Predict. Prepare. Prevent.**

[![Live Demo](https://img.shields.io/badge/Live-Demo-red?logo=streamlit)](https://eventpulse-ai.streamlit.app/)
[![Backend API](https://img.shields.io/badge/API-Render-blue?logo=render)](https://eventpulse-api-dpny.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Hackathon-success)]()
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/neekhilsingh/EventPulse-AI)

An AI-powered Traffic Incident Management System that predicts the priority of traffic incidents, recommends intelligent response strategies, allocates nearby emergency resources, and visualizes incidents through an interactive dashboard.

⭐ If you like this project, consider giving it a star on GitHub!

---

## 🏆 Hackathon Submission

**Team Name:** Kaizer

### 👥 Team Members

- **Neekhil Kumar Singh**
- **Harshit Agarwal (Team Lead)**

---

# 🌐 Live Demo

### 🚀 Streamlit Dashboard
👉 <https://eventpulse-ai.streamlit.app>

### ⚡ FastAPI Backend
👉 <https://eventpulse-api-dpny.onrender.com>

### 📖 API Documentation
👉 <https://eventpulse-api-dpny.onrender.com/docs>

---
# 📖 Overview

Traffic incidents often result in delayed emergency response, increased congestion, and inefficient resource utilization.

EventPulse-AI combines Machine Learning, intelligent recommendation systems, and geospatial intelligence to assist traffic authorities in making faster and more informed operational decisions.

The system predicts incident priority, estimates operational impact, recommends response strategies, identifies incident locations using reverse geocoding, allocates nearby emergency resources, and presents all insights through an interactive dashboard.

---

# ✨ Features

## 🤖 Machine Learning Priority Prediction

- Random Forest Classifier
- Predicts High / Low Priority incidents
- Confidence score for every prediction

---

## 🧠 AI Response Recommendation

Generates intelligent response plans including:

- Impact Score
- Impact Level
- Emergency Status
- Officers Required
- Barricades Required
- Diversion Recommendation
- Estimated Clearance Time
- Recommended Operational Actions

---

## 🗺 Reverse Geocoding

Integrated with **Mappls APIs**

Automatically converts geographic coordinates into human-readable addresses using the Mappls Reverse Geocoding API.

Example:

```
Kengeri Main Road,
Ambedkar Circle,
Bengaluru,
Karnataka
```

---

## 🚓 Emergency Resource Allocation

Suggests nearby emergency resources including:

- Police Station
- Hospital
- Fire Station

---

## 📊 Interactive Dashboard

Built using **Streamlit**

Features include:

- Incident Analysis
- Severity Meter
- AI Summary
- Resource Allocation
- Incident Timeline
- Interactive Map

---

# 🏗 System Architecture

```
                  User

                    │

                    ▼

          Streamlit Cloud Dashboard

                    │

                    ▼

             FastAPI Backend (Render)

                    │

      ┌─────────────┼─────────────┐

      ▼             ▼             ▼

Random Forest   Recommendation   Mappls API
   Model            Engine

      │             │             │

      └─────────────┼─────────────┘

                    ▼

        Emergency Resource Engine

                    │

                    ▼

          AI Decision Dashboard
```
Detailed architecture documentation is available in `docs/architecture.md`

---

# 🧠 Machine Learning Pipeline

## Data Processing

- Data Cleaning
- Missing Value Treatment
- Feature Engineering
- One-Hot Encoding
- Feature Alignment

---

## Model

**Random Forest Classifier**

Reasons for selection:

- Robust
- Handles mixed features
- Less overfitting
- High interpretability
- Excellent classification performance

---

## Recommendation Engine

A rule-based operational decision engine built on top of machine learning predictions that generates actionable response plans instead of only predicting incident priority.

---

# 🛠 Tech Stack

### Backend

- FastAPI
- Pydantic
- Joblib

### Machine Learning

- Scikit-learn
- Pandas
- NumPy

### Frontend

- Streamlit

### APIs

- Mappls Reverse Geocoding API
- REST APIs (FastAPI)

### Visualization

- Streamlit
- Pandas

### Deployment

- Render
- Streamlit Community Cloud

---

# 🔌 API Design

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health Check |
| POST | /predict | Predict incident priority and generate AI recommendations |

Detailed API documentation is available in `docs/api_design.md`.

---

# 📈 Results

- Model: Random Forest Classifier
- Priority Classification: High / Low
- Confidence Score Returned for Every Prediction
- Integrated End-to-End AI Decision Support Pipeline
- Successfully Deployed on Render and Streamlit Cloud

---

# 📂 Project Structure

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
├── .env
├── .gitignore
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
└── test_mappls.py
```


---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/neekhilsingh/EventPulse-AI.git
```

Move into the project

```bash
cd EventPulse-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
MAPPLS_API_KEY=YOUR_MAPPLS_API_KEY
```

---

# 💻 Run Locally

## Start Backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Start Frontend

```bash
streamlit run frontend/app.py
```

Frontend

```
http://localhost:8501
```

---

# ☁ Deployment

| Service | Platform |
|----------|----------|
| Frontend | Streamlit Community Cloud |
| Backend | Render |
| ML Model | Joblib (.pkl) |
| Reverse Geocoding | Mappls API |

---
# 📸 Screenshots

## 🏠 Dashboard
![Dashboard](screenshots/Dashboard.png)

---

## 🔮 Prediction Result
![Prediction](screenshots/Prediction.png)

---

## 🧠 AI Recommendation
![AI Recommendation](screenshots/AI_Recommendation.png)

---

## 🚓 Emergency Resource Allocation
![Emergency Resources](screenshots/Emergency_Resource.png)

---

# 🗺️ Interactive Map
![Interactive Map](screenshots/Interactive_Map.png)

---

# 🎯 Impact

EventPulse-AI enables authorities to:

- Improve emergency response time
- Reduce traffic congestion
- Optimize emergency resource allocation
- Support operational decision-making
- Improve situational awareness
- Enable AI-assisted traffic incident management

---

# 🔮 Future Scope

The architecture has been designed to support future integration with real-time traffic and smart city infrastructure.

- Live Traffic API Integration
- CCTV-based Incident Detection
- GPS Vehicle Tracking
- Deep Learning Prediction Models
- Automatic Route Optimization
- Emergency Vehicle Tracking
- Push Notifications
- Mobile Application
- Smart City Integration

---



# 👨‍💻 Team Kaizer

**Harshit Agarwal** — Team Lead

**Neekhil Kumar Singh**

---

# 📜 License

This project was developed as part of the Flipkart Gridlock Hackathon 2.0 and is intended for educational, research, and demonstration purposes.

---

# ⭐ Thank You

If you found this project interesting, consider giving the repository a ⭐.

**EventPulse-AI**

### Predict. Prepare. Prevent.

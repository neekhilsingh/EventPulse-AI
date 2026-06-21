# 🚦 EventPulse-AI

> **Predict. Prepare. Prevent.**

An AI-powered Traffic Incident Management System that predicts the priority of traffic incidents, recommends intelligent response strategies, allocates nearby emergency resources, and visualizes incidents through an interactive dashboard.

---

## 🏆 Hackathon Submission

**Team Name:** Kaizer

### 👥 Team Members

- **Neekhil Kumar Singh**
- **Harshit Agarwal (Team Lead)**

---

# 🌐 Live Demo

### 🚀 Streamlit Dashboard

https://eventpulse-ai.streamlit.app/

### ⚡ FastAPI Backend

https://eventpulse-api-dpny.onrender.com/

### 📖 API Documentation

https://eventpulse-api-dpny.onrender.com/docs

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

Automatically converts latitude and longitude into human-readable addresses.

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

### Visualization

- Streamlit
- Pandas

### Deployment

- Render
- Streamlit Community Cloud

---

# 📂 Project Structure

```
EventPulse-AI

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

---

# ▶ Run Backend

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

# ▶ Run Frontend

```bash
streamlit run frontend/app.py
```

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

This project was developed as part of a hackathon submission and is intended for educational and research purposes.

---

# ⭐ EventPulse-AI

### **Predict. Prepare. Prevent.**

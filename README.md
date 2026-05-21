# Financial Risk Analysis System

A Machine Learning-powered web application that predicts whether a loan applicant is **HIGH RISK** or **LOW RISK** using financial and personal attributes.

---

## Project Overview

The Financial Risk Analysis System helps analyze customer financial risk using Machine Learning models trained on financial datasets.

The system predicts loan default probability and classifies applicants into:

- **LOW RISK**
- **HIGH RISK**

This project demonstrates complete ML deployment from data preprocessing to real-time web prediction using FastAPI.

---

## Features

- Financial risk prediction
- High / Low risk classification
- FastAPI backend API
- Interactive web frontend
- Real-time prediction system
- ML model comparison and selection

---

## Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Joblib

### Frontend
- HTML
- CSS
- JavaScript

---

## Machine Learning Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

---

## Model Accuracy

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 97.3% |
| Decision Tree | 100% |
| Random Forest | 100% |

Best model is automatically selected and deployed.

---

## Dataset Improvement

Original dataset had severe imbalance:

- Low Risk: 4999
- High Risk: 1

Balanced dataset after preprocessing:

- Low Risk: 3153
- High Risk: 1847

This improved model performance and generalization.

---

## Project Structure

```plaintext
Major Project(ML)
│
├── data
│   ├── Financial Risk Classification Dataset.csv
│   └── balanced_data.csv
│
├── model_training
│   ├── fix_dataset.py
│   ├── preprocess.py
│   ├── train.py
│   ├── model.pkl
│   ├── scaler.pkl
│   └── data.pkl
│
├── backend
│   └── app.py
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone (https://github.com/brahmmareddy-123/financial-risk-analysis-system.git)
```

Move into project:

```bash
cd financial-risk-analysis-system
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn backend.app:app
```

Backend URL:

```plaintext
http://127.0.0.1:8000
```

API Docs:

```plaintext
http://127.0.0.1:8000/docs
```

---

## Run Frontend

Open:

```plaintext
frontend/index.html
```

---

## User Inputs

- Age
- Annual Income
- Education Years
- Work Experience
- Credit Score

Output:

- HIGH RISK
- LOW RISK

---

## Future Improvements

- Google Cloud deployment
- Dashboard analytics
- User authentication
- Database integration
- Advanced financial visualizations

---

## Author

**BANDI BRAHMMA REDDY**

Machine Learning Major Project  
Financial Risk Analysis System

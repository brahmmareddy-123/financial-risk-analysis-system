from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
from fastapi import Body


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model_training/model.pkl")
scaler = joblib.load("model_training/scaler.pkl")


@app.get("/")
def home():
    return {"message": "Financial Risk API Running"}



@app.post("/predict")
def predict(data: list = Body(...)):

    data = np.array([data])

    scaled = scaler.transform(data)

    prediction = model.predict(scaled)

    risk = "HIGH RISK" if prediction[0] == 1 else "LOW RISK"

    return {"prediction": risk}
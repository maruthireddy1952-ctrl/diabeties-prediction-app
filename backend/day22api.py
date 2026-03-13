from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np

app=FastAPI()
model=joblib.load("diabetes.pkl")


class Features(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "AI Prediction API Running"}

@app.post("/predict")
def predict(data: Features):
    try:
        prediction = model.predict([data.features])
        return {"Prediction": prediction.tolist()}
    except Exception as e:
        return {"Error":str(e)}

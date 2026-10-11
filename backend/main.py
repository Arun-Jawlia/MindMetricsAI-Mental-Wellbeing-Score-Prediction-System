import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

model = joblib.load("../ml/model/Mental_Health_Model.pkl")

#Pyndantic Model
class StudentData(BaseModel):
    Age:int
    Gender:str
    Country:str
    Academic_Level:str
    Most_Used_Platform:str
    Purpose_Of_Use:str
    Avg_Daily_Usage_Hours:float
    Daily_Unlocks:int
    Study_Hours:float
    Physical_Activity_Hours:float
    Sleep_Hours_Per_Night:float
    Stress_Level:float

app = FastAPI()

@app.get('/')
def greet():
    return {
        "msg":"Welcome to MindMetrics: AI-Powered Mental Score Prediction System",
        "status":"Working"
    }
@app.post("/predict")
def predict(data: StudentData):
    pass
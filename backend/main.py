#pylint:disable=all
import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

from typing import Literal

model = joblib.load("../ml/model/Mental_Health_Model.pkl")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

top_countries = ['Other',
 'India',
 'USA',
 'Canada',
 'Australia',
 'UK',
 'Germany',
 'Mexico',
 'Turkey',
 'France']  

#Pyndantic Model
class StudentData(BaseModel):
    age:int = Field(..., ge=10, le=100)
    gender:str = Literal["Male", 'Female']
    country:str 
    academic_level: str = Literal['Undergraduate', 'Graduate', "High School"]
    most_used_platform: Literal['Facebook','LinkedIn','Instagram','Snapchat','Twitter','YouTube','TikTok','LINE','KakaoTalk','VKontakte','WhatsApp','WeChat']
    purpose_of_use: Literal['Networking', 'Education', 'Entertainment', 'News']
    avg_daily_usage_hours:float = Field(..., ge=0, le=24)
    daily_unlocks:int = Field(..., ge=0)
    study_hours:float = Field(..., ge=0, le=24)
    physical_activity_hours:float = Field(..., ge=0, le=24)
    sleep_hours_per_night:float = Field(..., ge=0, le=24)
    stress_level:str= Literal['Medium', 'Low', 'Very High', 'High']


# Describe what we send back
class PredictionResponse(BaseModel):
    predicted_mental_health_score: float


@app.get('/')
def greet():
    return {
        "msg":"Welcome to MindMetrics: AI-Powered Mental Score Prediction System",
        "status":"Working"
    }


@app.post("/predict", response_model = PredictionResponse)
def predict(data: StudentData):

    country_group = data.country if data.country in top_countries else 'Other'

    input_row = pd.DataFrame([{
        "Age": data.age,
        "Gender":data.gender,
        "Country": data.country,
        "Academic_Level": data.academic_level,
        "Most_Used_Platform": data.most_used_platform,
        "Purpose_Of_Use": data.purpose_of_use,
        "Avg_Daily_Usage_Hours":data.avg_daily_usage_hours,
        "Daily_Unlocks": data.daily_unlocks,
        "Study_Hours": data.study_hours,
        "Physical_Activity_Hours":data.physical_activity_hours,
        "Sleep_Hours_Per_Night":data.sleep_hours_per_night,
        "Stress_Level":data.stress_level,
        "Grouped_country": country_group
    }])

    prediction = model.predict(input_row)[0]

    return PredictionResponse(predicted_mental_health_score = round(float(prediction),2))
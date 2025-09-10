from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS so frontend (React, Next.js, etc.) can fetch API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello from FastAPI backend!"}

@app.get("/data")
def get_data():
   sample_data = [
        {
            "city": "Delhi",
            "temperature": 32,
            "status": "Sunny",
            "aqi": 120
        },
        {
            "city": "Mumbai",
            "temperature": 30,
            "status": "Cloudy",
            "aqi": 140
        },
        {
            "city": "Chennai",
            "temperature": 34,
            "status": "Humid",
            "aqi": 110
        },
        {
            "city": "Kolkata",
            "temperature": 31,
            "status": "Rainy",
            "aqi": 135
        }
    ]
    return sample_data

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
    sample_data = {
        "city": "Delhi",
        "temperature": 32,
        "status": "Sunny",
        "aqi": 120
    }
    return sample_data

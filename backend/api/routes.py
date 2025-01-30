from fastapi import FastAPI
from backend.services.resource_allocation import allocate_resources
from ai_models.predict_delays import predict_delays

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Middleware API is running"}

@app.post("/allocate_resources/")
def allocate(data: dict):
    result = allocate_resources(data)
    return {"allocation": result}

@app.post("/predict_delay/")
def predict(data: dict):
    prediction = predict_delays(data)
    return {"predicted_delay": prediction}
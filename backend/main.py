from fastapi import FastAPI
from api.routes import router

app = FastAPI()

# Register API routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Aerospace Resource Optimization API"}

# Run with `uvicorn main:app --reload`

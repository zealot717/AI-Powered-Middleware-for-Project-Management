import random
from backend.models.models import Task
from sqlalchemy.orm import Session

def predict_delay_risk(tasks):
    risk_predictions = {}

    for task in tasks:
        risk = random.uniform(0, 1)  # Random risk probability (placeholder)
        risk_predictions[task.id] = risk

    return risk_predictions

def analyze_risks(db: Session):
    tasks = db.query(Task).all()
    risks = predict_delay_risk(tasks)

    db.commit()  
    return risks

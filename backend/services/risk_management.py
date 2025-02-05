from sqlalchemy.orm import Session
from ai_models.predict_delays import analyze_risks

def predict_project_risks(db: Session):
    return analyze_risks(db)

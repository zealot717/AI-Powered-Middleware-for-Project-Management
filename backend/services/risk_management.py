from sqlalchemy.orm import Session
from ai_models.risk_analysis import analyze_risks
from models.models import RiskAssessmentResults

def predict_project_risks(db: Session):
    """Runs AI-based risk analysis and saves results."""
    risk_data = analyze_risks(db)

    if not risk_data:
        return []

    # Store AI results in the database
    for project_id, risk_score in risk_data.items():
        risk_entry = RiskAssessmentResults(
            project_id=project_id,
            risk_score=risk_score,
            risk_factors="AI-predicted delay risks"  # You can expand this with real data
        )
        db.add(risk_entry)

    db.commit()
    return db.query(RiskAssessmentResults).all()
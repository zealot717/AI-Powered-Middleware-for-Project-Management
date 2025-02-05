from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db_connection import get_db
from models.models import OptimizedResourceAllocation, RiskAssessmentResults
from middleware.ai_engine import process_optimized_allocation, process_risk_assessment

router = APIRouter()

@router.post("/run_optimization/{project_id}")
def run_optimization(project_id: str, db: Session = Depends(get_db)):
    """Triggers AI optimization for a project."""
    process_optimized_allocation(project_id)
    return {"message": "Optimization completed and stored in the database."}

@router.post("/run_risk_assessment/{project_id}")
def run_risk_assessment(project_id: str, db: Session = Depends(get_db)):
    """Triggers AI risk assessment for a project."""
    process_risk_assessment(project_id)
    return {"message": "Risk assessment completed and stored in the database."}

@router.get("/get_optimized_resources/{project_id}")
def get_optimized_resources(project_id: str, db: Session = Depends(get_db)):
    """Fetches AI-optimized resource allocation for a project."""
    results = db.query(OptimizedResourceAllocation).filter_by(project_id=project_id).all()
    return results

@router.get("/get_risk_assessment/{project_id}")
def get_risk_assessment(project_id: str, db: Session = Depends(get_db)):
    """Fetches AI-generated risk assessment results for a project."""
    result = db.query(RiskAssessmentResults).filter_by(project_id=project_id).first()
    return result

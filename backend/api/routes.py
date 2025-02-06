from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_connection import get_db
from models.models import Project
from services.resource_allocation import allocate_resources
from services.risk_management import predict_project_risks
from ai_models.optimize_resources import optimize_project_resources  

router = APIRouter()

# ✅ Get all projects
@router.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    """Fetch all projects from the database."""
    projects = db.query(Project).all()
    if not projects:
        raise HTTPException(status_code=404, detail="No projects found")
    
    return [{"project_id": p.project_id, "project_name": p.project_name, "budget": p.budget, "end_date": p.end_date, "status": p.status} for p in projects]

# ✅ AI Analysis - Resource Optimization & Risk Estimation
@router.get("/ai-analysis")
def get_ai_analysis(db: Session = Depends(get_db)):
    """Fetch AI-generated resource allocation and risk prediction."""
    analysis = optimize_project_resources(db)  
    if not analysis or "OptimizedResources" not in analysis:
        raise HTTPException(status_code=404, detail="AI analysis data not available")
    
    return {
        "optimizedAllocations": analysis.get("OptimizedResources", []),
        "riskPrediction": analysis.get("RiskPrediction", "No data available"),
    }


# ✅ Risk Analysis - Returns actual AI risk predictions
@router.get("/risk-analysis")
def get_risk_analysis(db: Session = Depends(get_db)):
    """Fetch AI-based risk analysis details."""
    risks = predict_project_risks(db)  # Calls AI model for risk analysis
    if not risks:
        raise HTTPException(status_code=404, detail="No risk data available")

    return [{"project_id": r.project_id, "risk_score": r.risk_score, "risk_factors": r.risk_factors} for r in risks]

@router.get("/allocations")
def get_allocations(db: Session = Depends(get_db)):
    """Fetch AI-generated resource allocations."""
    allocations = allocate_resources(db)  # Calls AI-based optimizer
    if not allocations or "OptimizedResources" not in allocations:
        raise HTTPException(status_code=404, detail="No allocation data available")

    return allocations["OptimizedResources"]
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db_connection import get_db
from models.models import Project
from services.resource_allocation import allocate_resources
from services.risk_management import predict_project_risks

router = APIRouter()

# Get all projects
@router.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects

# Get a single project by ID
@router.get("/projects/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return {"error": "Project not found"}
    return project

# Trigger AI resource allocation
@router.post("/allocate")
def allocate_resources_endpoint(db: Session = Depends(get_db)):
    allocation = allocate_resources(db)
    return {"message": "Resource allocation completed", "allocation": allocation}

# Trigger AI risk prediction
@router.post("/predict-risks")
def predict_risks_endpoint(db: Session = Depends(get_db)):
    risks = predict_project_risks(db)
    return {"message": "Risk prediction completed", "risks": risks}


@router.get("/ai-analysis")
def get_ai_analysis(db: Session = Depends(get_db)):
    try:
        result = allocate_resources(db)  # Ensure this function is implemented
        return {"optimizedAllocations": result["allocations"], "riskPrediction": result["risks"]}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/risk-analysis")
def get_risk_analysis():
    return {"risks": ["Budget Overruns", "Schedule Delays", "Resource Shortages"]}

@router.get("/allocations")
def get_allocations():
    return {"allocations": [{"project_id": 1, "resources": "Engineers: 5, Analysts: 3"}]}


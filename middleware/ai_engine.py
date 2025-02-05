from database.db_connection import SessionLocal
from models.models import OptimizedResourceAllocation, RiskAssessmentResults
from backend.ai_models.optimize_resources import optimize_resources
from backend.ai_models.risk_analysis import assess_project_risk

def process_optimized_allocation(project_id):
    """Runs AI optimization and stores results in the database."""
    session = SessionLocal()
    try:
        optimized_results = optimize_resources(project_id)
        for result in optimized_results:
            allocation = OptimizedResourceAllocation(
                project_id=project_id,
                resource_id=result["resource_id"],
                allocated_hours=result["allocated_hours"],
                efficiency_score=result["efficiency_score"]
            )
            session.add(allocation)
        session.commit()
    finally:
        session.close()

def process_risk_assessment(project_id):
    """Runs AI risk assessment and stores results in the database."""
    session = SessionLocal()
    try:
        risk_score, risk_factors = assess_project_risk(project_id)
        risk_entry = RiskAssessmentResults(
            project_id=project_id,
            risk_score=risk_score,
            risk_factors=", ".join(risk_factors)
        )
        session.add(risk_entry)
        session.commit()
    finally:
        session.close()

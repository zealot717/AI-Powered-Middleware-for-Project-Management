from sqlalchemy.orm import Session
from ai_models.optimize_resources import optimize_project_resources
from models.models import OptimizedResourceAllocation

def allocate_resources(db: Session):
    """Runs AI-based resource allocation and saves results."""
    allocation_data = optimize_project_resources(db)

    if not allocation_data or "OptimizedResources" not in allocation_data:
        return {"OptimizedResources": []}

    # Store AI results in the database
    for alloc in allocation_data["OptimizedResources"]:
        alloc_entry = OptimizedResourceAllocation(
            project_id=alloc["ProjectID"],
            resource_id=alloc["AssignedResource"],
            allocated_hours=40,  # Placeholder
            efficiency_score=0.85  # Placeholder
        )
        db.add(alloc_entry)

    db.commit()
    return db.query(OptimizedResourceAllocation).all()

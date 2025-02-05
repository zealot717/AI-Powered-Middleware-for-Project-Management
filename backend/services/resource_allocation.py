from sqlalchemy.orm import Session
from ai_models.optimize_resources import optimize_resource_allocation

def allocate_resources(db: Session):
    return optimize_resource_allocation(db)

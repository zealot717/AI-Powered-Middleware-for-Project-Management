from celery import Celery
from database.db_connection import SessionLocal
from services.resource_allocation import allocate_resources
from services.risk_management import predict_project_risks

celery = Celery("tasks", broker="redis://localhost:6379/0")

@celery.task
def async_allocate_resources():
    db = SessionLocal()
    allocation = allocate_resources(db)
    db.close()
    return allocation

@celery.task
def async_predict_risks():
    db = SessionLocal()
    risks = predict_project_risks(db)
    db.close()
    return risks
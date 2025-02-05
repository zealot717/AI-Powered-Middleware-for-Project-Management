from backend.ai_models.optimize_resources import optimize_resource_allocation
from backend.database.db_connection import SessionLocal
from backend.models.models import Task, Resource

def test_resource_optimization():
    db = SessionLocal()
    tasks = db.query(Task).all()
    resources = db.query(Resource).all()
    allocation = optimize_resource_allocation(db)
    
    assert isinstance(allocation, dict), "Allocation should be a dictionary"
    assert all(task.id in allocation for task in tasks), "All tasks should have an assigned resource"
    
    print("Resource Optimization Test Passed!")

if __name__ == "__main__":
    test_resource_optimization()

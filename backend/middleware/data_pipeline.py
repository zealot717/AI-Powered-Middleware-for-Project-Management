from sap_connector import get_oauth_token, get_sap_data
from backend.database import db_connection
from backend.models import models
def initialize_database():
    """
    Creates database tables if they do not exist.
    """
    db_connection.Base.metadata.create_all(bind=db_connection.engine)

def load_mock_data():
    """
    Extracts mock SAP data, transforms it, and loads it into the database.
    """
    token = get_oauth_token()
    sap_data = get_sap_data(token, "projects")
    
    session = db_connection.SessionLocal()
    try:
        for project in sap_data:
            project_entry = models.Project(
                id=project["ProjectID"],
                name=project["ProjectName"],
                start_date=project["StartDate"],
                end_date=project["EndDate"],
                status=project["Status"],
                budget=project["Budget"]
            )
            session.add(project_entry)
            
            for resource in project["AllocatedResources"]:
                resource_entry = models.Resource(
                    id=resource["ResourceID"],
                    name=resource["Name"],
                    role=resource["Role"],
                    availability=resource["Availability"],
                    project_id=project["ProjectID"]
                )
                session.add(resource_entry)
            
            for task in project["Tasks"]:
                task_entry = models.Task(
                    id=task["TaskID"],
                    name=task["TaskName"],
                    start_date=task["StartDate"],
                    end_date=task["EndDate"],
                    assigned_resource_id=task["AssignedResource"],
                    project_id=project["ProjectID"]
                )
                session.add(task_entry)
        
        session.commit()
        print("Mock data successfully loaded into the database.")
    except Exception as e:
        session.rollback()
        print(f"Error loading data: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    initialize_database()
    load_mock_data()

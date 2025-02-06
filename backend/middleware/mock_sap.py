import json
import random
from datetime import datetime, timedelta
from database.db_connection import SessionLocal
from models.models import Project, Resource, Task

def generate_mock_sap_projects(num_projects=5):
    """Generates mock SAP project management data resembling real SAP structures."""
    projects = []
    for i in range(1, num_projects + 1):
        start_date = datetime.now() - timedelta(days=random.randint(30, 180))
        end_date = start_date + timedelta(days=random.randint(30, 365))
        project = {
            "ProjectID": f"P-{1000 + i}",
            "ProjectName": f"Aerospace Project {i}",
            "StartDate": start_date.strftime("%Y-%m-%d"),
            "EndDate": end_date.strftime("%Y-%m-%d"),
            "Status": random.choice(["Planned", "In Progress", "Completed"]),
            "Budget": round(random.uniform(1_000_000, 10_000_000), 2),
            "AllocatedResources": generate_mock_resources(random.randint(3, 10)),
            "Tasks": generate_mock_tasks(random.randint(5, 15), start_date, end_date)
        }
        projects.append(project)
    return projects

def generate_mock_resources(num_resources):
    """Generates mock aerospace project resources."""
    roles = ["Engineer", "Scientist", "Technician", "Analyst", "Project Manager"]
    return [
        {
            "ResourceID": f"R-{1000 + i}",
            "Name": f"Resource {i}",
            "Role": random.choice(roles),
            "Availability": random.randint(50, 100)
        }
        for i in range(num_resources)
    ]

def generate_mock_tasks(num_tasks, start_date, end_date):
    """Generates mock aerospace project tasks."""
    return [
        {
            "TaskID": f"T-{1000 + i}",
            "TaskName": f"Task {i}",
            "StartDate": (start_date + timedelta(days=random.randint(0, (end_date - start_date).days // 2))).strftime("%Y-%m-%d"),
            "EndDate": (start_date + timedelta(days=random.randint((end_date - start_date).days // 2, (end_date - start_date).days))).strftime("%Y-%m-%d"),
            "AssignedResource": f"R-{1000 + random.randint(1, 20)}"
        }
        for i in range(num_tasks)
    ]

def store_mock_data_in_db():
    """Stores mock SAP data into the database."""
    session = SessionLocal()
    mock_projects = generate_mock_sap_projects()
    for project in mock_projects:
        db_project = Project(
            project_id=project["ProjectID"],
            project_name=project["ProjectName"],
            start_date=project["StartDate"],
            end_date=project["EndDate"],
            status=project["Status"],
            budget=project["Budget"]
        )
        session.add(db_project)
        for resource in project["AllocatedResources"]:
            db_resource = Resource(
                resource_id=resource["ResourceID"],
                name=resource["Name"],
                role=resource["Role"],
                availability=resource["Availability"],
                project_id=db_project.project_id
            )
            session.add(db_resource)
        for task in project["Tasks"]:
            db_task = Task(
                task_id=task["TaskID"],
                task_name=task["TaskName"],
                start_date=task["StartDate"],
                end_date=task["EndDate"],
                assigned_resource=task["AssignedResource"],
                project_id=db_project.project_id
            )
            session.add(db_task)
    session.commit()
    session.close()

def fetch_mock_sap_data():
    """Simulates API fetch for SAP project data by returning mock data."""
    return generate_mock_sap_projects()

if __name__ == "__main__":
    store_mock_data_in_db()
    mock_data = fetch_mock_sap_data()
    print(json.dumps(mock_data, indent=4))

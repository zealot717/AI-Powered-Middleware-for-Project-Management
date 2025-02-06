import json
import random
from datetime import datetime, timedelta
from database.db_connection import SessionLocal  # Import your DB session
from models.models import Project, Resource, Task

def generate_mock_sap_projects(num_projects=5):
    projects = []
    for i in range(1, num_projects + 1):
        start_date = datetime.now() - timedelta(days=random.randint(30, 180))
        end_date = start_date + timedelta(days=random.randint(365, 730))  # Longer project durations
        project_id = f"P-{1000 + i}"  # Store project ID for consistency
        project = {
            "ProjectID": project_id,  # Use stored ID
            "ProjectName": f"Aerospace Project {i}",
            "StartDate": start_date.strftime("%Y-%m-%d"),
            "EndDate": end_date.strftime("%Y-%m-%d"),
            "Status": random.choice(["Planned", "In Progress", "Completed", "Delayed"]),
            "Budget": round(random.uniform(10_000_000, 100_000_000), 2),  # Increased budget
            "AllocatedResources": generate_mock_resources(random.randint(5, 15), project_id),  # Pass ID
            "Tasks": generate_mock_tasks(random.randint(10, 30), start_date, end_date, project_id)  # Pass ID
        }
        projects.append(project)
    return projects

def generate_mock_resources(num_resources, project_id):
    roles = ["Engineer", "Scientist", "Technician", "Analyst", "Project Manager"]
    return [
        {
            "ResourceID": f"R-{project_id}-{i}",  # Unique ID using project_id
            "Name": f"Resource {i}",
            "Role": random.choice(roles),
            "Availability": random.randint(50, 100)
        }
        for i in range(num_resources)
    ]

def generate_mock_tasks(num_tasks, start_date, end_date, project_id):
    resource_ids_for_project = [f"R-{project_id}-{i}" for i in range(15)] # Generate all possible resources for task assignment
    return [
        {
            "TaskID": f"T-{project_id}-{i}",  # Unique ID using project_id
            "TaskName": f"Task {i}",
            "StartDate": (start_date + timedelta(days=random.randint(0, (end_date - start_date).days // 2))).strftime("%Y-%m-%d"),
            "EndDate": (start_date + timedelta(days=random.randint((end_date - start_date).days // 2, (end_date - start_date).days))).strftime("%Y-%m-%d"),
            "AssignedResource": random.choice(resource_ids_for_project) # Choose from project's resources
        }
        for i in range(num_tasks)
    ]


def store_mock_data_in_db():
    session = SessionLocal()
    mock_projects = generate_mock_sap_projects()
    try:
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
        print("Mock data stored successfully.")
    except Exception as e:  # Catch potential errors during database operations
        session.rollback()  # Rollback changes in case of error
        print(f"Error storing mock data: {e}")
    finally:
        session.close()


def fetch_mock_sap_data():
    return generate_mock_sap_projects()

if __name__ == "__main__":
    store_mock_data_in_db()  # Store the data in the database
    mock_data = fetch_mock_sap_data()  # Then, you can fetch it
    print(json.dumps(mock_data, indent=4))
import requests

def fetch_project_data():
    try:
        response = requests.get("https://sap-system.example.com/projects")
        return response.json()
    except:
        return {"project_id": 123, "workers": 50, "materials": 200, "deadlines": 45}
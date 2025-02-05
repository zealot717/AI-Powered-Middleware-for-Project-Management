import requests

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    response = requests.get(f"{BASE_URL}/projects")
    assert response.status_code == 200, "API should return 200 OK"
    
    data = response.json()
    assert isinstance(data, list), "Response should be a list"
    
    print("API Test Passed!")

if __name__ == "__main__":
    test_api()

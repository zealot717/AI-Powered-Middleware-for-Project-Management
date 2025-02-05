# tests/test_sap_integration.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from middleware.sap_connector import get_oauth_token, get_sap_data
from middleware.ai_engine import run_ai_logic

def test_oauth_token():
    """Test if OAuth token retrieval works"""
    token = get_oauth_token()
    assert token is not None, "Failed to retrieve OAuth token"
    print("OAuth token successfully retrieved!")

def test_sap_api_integration():
    """Test if SAP API integration is successful"""
    token = get_oauth_token()
    project_data = get_sap_data(token, 'projects')  # Fetch the specific endpoint data
    assert project_data is not None, "Failed to retrieve project data from SAP"
    print("SAP API successfully integrated, project data fetched.")

def test_ai_integration():
    """Test the entire flow, from SAP data to AI model execution"""
    results = run_ai_logic()
    assert results is not None, "AI model execution failed"
    print("AI model successfully executed, results returned.")

if __name__ == "__main__":
    test_oauth_token()
    test_sap_api_integration()
    test_ai_integration()

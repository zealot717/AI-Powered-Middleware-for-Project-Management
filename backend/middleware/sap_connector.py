import json
from mock_sap import fetch_mock_sap_data

def get_oauth_token():
    """
    Simulates retrieving an OAuth token.
    Since we are using mock data, return a static token.
    """
    return "mock_oauth_token_12345"

def get_sap_data(token: str, endpoint: str):
    """
    Simulates fetching data from SAP using mock data.
    :param token: OAuth token (not used in mock version)
    :param endpoint: The endpoint to fetch data from
    :return: Mock SAP data in JSON format
    """
    if token != "mock_oauth_token_12345":
        raise ValueError("Invalid OAuth token")
    
    if endpoint == "projects":
        return fetch_mock_sap_data()
    else:
        raise ValueError(f"Unsupported endpoint: {endpoint}")

if __name__ == "__main__":
    token = get_oauth_token()
    sap_data = get_sap_data(token, "projects")
    print(json.dumps(sap_data, indent=4))

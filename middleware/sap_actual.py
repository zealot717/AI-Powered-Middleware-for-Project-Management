import requests
from config.sap_config import SAP_CLIENT_ID, SAP_CLIENT_SECRET, SAP_TOKEN_URL

def get_oauth_token():
    """
    Retrieves an OAuth token using the client credentials.
    """
    payload = {
        'grant_type': 'client_credentials',
        'client_id': SAP_CLIENT_ID,
        'client_secret': SAP_CLIENT_SECRET
    }
    
    response = requests.post(SAP_TOKEN_URL, data=payload)
    
    if response.status_code == 200:
        token_data = response.json()
        return token_data['access_token']
    else:
        raise Exception(f"Failed to get OAuth token: {response.status_code} - {response.text}")
    
def get_sap_data(oauth_token, endpoint):
    """
    Makes a GET request to the SAP API using the OAuth token.
    
    Args:
        oauth_token (str): The OAuth token for authorization.
        endpoint (str): The specific SAP API endpoint to hit (e.g., project data, resource allocation).
        
    Returns:
        dict: The response data from the SAP API.
    """
    headers = {'Authorization': f'Bearer {oauth_token}'}
    url = f'{SAP_API_BASE_URL}/{endpoint}'  # Construct the full URL for the SAP endpoint
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from SAP API: {response.status_code} - {response.text}")
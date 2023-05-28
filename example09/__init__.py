import requests

def fetch_data():
    response = requests.get('https://example.com')
    return response.json()

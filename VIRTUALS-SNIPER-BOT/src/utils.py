import requests

def fetch_opportunities(api_key):
    url = "https://api.virtuals.io/sniper-opportunities"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    return response.json()

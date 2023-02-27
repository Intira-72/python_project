# API = Application Programming Interface

import requests

endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint)
# HTTP Request -> HTML
# REST API HTTP Request -> JSON

if __name__=="__main__":
    if get_response.status_code == 200:
        print(get_response.json())
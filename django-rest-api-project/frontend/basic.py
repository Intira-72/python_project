# API = Application Programming Interface

import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,
                             json={"title": "12354",
                                   "content": "Hello World",
                                   "price": "abc123"})
# HTTP Request -> HTML
# REST API HTTP Request -> JSON

if __name__=="__main__":
    print(get_response.json())
        
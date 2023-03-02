import requests

endpoint = "http://localhost:8000/api/product/"

data = {'title': 'Hello World 7',
        'content': None,
        'price': '88.88'}


get_response = requests.post(endpoint, json=data)


if __name__=="__main__":
    print(get_response.json())
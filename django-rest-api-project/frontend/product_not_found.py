import requests

endpoint = "http://localhost:8000/api/product/1123/"

get_response = requests.get(endpoint)


if __name__=="__main__":
    print(get_response.json())
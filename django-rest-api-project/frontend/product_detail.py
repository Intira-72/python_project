import requests

endpoint = "http://localhost:8000/api/product/1/"

get_response = requests.get(endpoint)


if __name__=="__main__":
    print(get_response.json())
import requests


endpoint:str = "http://localhost:8000/api/products/6666666/"

get_response = requests.get(endpoint) 

print(get_response.json())


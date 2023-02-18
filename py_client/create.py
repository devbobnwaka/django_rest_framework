import requests


endpoint:str = "http://localhost:8000/api/products/"

headers = {'Authorization': 'Bearer 2f1e299ef94dd7f2bf4771c3a8f50cecf9569448'}
data = {
    "title": "This field is done!!!"
}
get_response = requests.post(endpoint, json=data) 

print(get_response.json())


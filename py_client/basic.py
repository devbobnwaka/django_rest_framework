import requests

# endpoint:str = "https://httpbin.org/status/200"
# endpoint:str = "http://httpbin.org/anything"
endpoint:str = "http://localhost:8000/api/" #http:// 127.0.0.1:8000/ #django project address

get_response = requests.get(endpoint, params={'abc':123}, json={'query':"Hello world"}) #HTTP REQUEST
# print(get_response.text) #print raw text response
# print(get_response.json()) #print response in django dictionary
# print(get_response.status_code)
"""
HTTP REQUEST -> HTML
REST API HTTP REQUEST -> JSON/XML

JavaScript Object Notation ~ Python Dictionary
"""
# Test my django api
# print(get_response.text)
# print(get_response.json()['message'])
print(get_response.json())
# print(get_response.status_code)

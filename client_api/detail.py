import requests

endpoint = "http://127.0.0.1:8081/product/detail/1/"
response = requests.get(endpoint)
print(response.json())
print(response.status_code) 


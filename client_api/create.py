import requests

endpoint = "http://127.0.0.1:8081/product/create-product/"
response = requests.post(endpoint,json={"name" :"Mandarine 1", "content" : "", "price" : 200 })
print(response.json())
print(response.status_code) 

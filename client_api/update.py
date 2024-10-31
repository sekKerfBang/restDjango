import requests

endpoint = "http://127.0.0.1:8081/product/update-product/3/"
response = requests.put(endpoint,json={ "name" : "Mangue Guineen", "content" : "", "price" : 10000 })
print(response.json())  
print(response.status_code) 

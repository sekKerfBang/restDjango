import requests

id = input("enter id product that you want to delete : \n")
endpoint = f"http://127.0.0.1:8081/product/delete-product/{id}/"
response = requests.delete(endpoint)
print(response.status_code, response.status_code==204) 
import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8081/api/auth/"
username = input('Enter your username :\n')
password = getpass('Enter your password : \n')
auth_response = requests.post(endpoint, json={'username' : username, 'password' : password})
print(auth_response.json())
print(auth_response.status_code)

if auth_response.status_code == 200:
    endpoint = "http://127.0.0.1:8081/product/list-product/"
    headers = {
        'Authorization':'Beaver 0c20abe2c61aed2429867b8d5f761abbd6588ad3'
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code) 

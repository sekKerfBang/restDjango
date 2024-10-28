import requests

endpoint = "http://127.0.0.1:8081/product/"
response = requests.post(endpoint, json={"name":"Ananas", "content" : "just Pasteque", "price" : 20})
print(response.json())
print(response.status_code)   

# HTTP requests --> HTML
# REST API HTTP --> JSON JAVASCRIPT OBJECT NOTATION

# {
#     'args': {},
#     'data': '',
#     'files': {},
#     'form': {},
#     'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-67178cb5-75058ca93f2e27352d0a5375'},
#     'json': None,
#     'method': 'GET',
#     'origin': '41.223.48.14',
#     'url': 'http://httpbin.org/anything'
#     }
# {
#     "args": {}, 
#     "data": "", 
#     "files": {}, 
#     "form": {}, 
#     "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.32.3", 
#     "X-Amzn-Trace-Id": "Root=1-67178d2d-1bce0faf7712539965ad1e55"
# }, 
#     "json": null, 
#     "method": "GET", 
#     "origin": "41.223.48.14", 
#     "url": "http://httpbin.org/anything"
# }

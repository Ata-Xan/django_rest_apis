import requests


endpoint = "http://localhost:8001/api/products/2"
# params ===> url/?arg=value ===> like here it is like: http://localhost:8001/api/?abc=123
get_response = requests.get(endpoint)
print(get_response.json())

import requests


endpoint = "http://localhost:8001/api/"
# params ===> url/?arg=value ===> like here it is like: http://localhost:8001/api/?abc=123
get_response = requests.post(endpoint, json={"content":"hello world"})
print(get_response.json())
# print(get_response.status_code)
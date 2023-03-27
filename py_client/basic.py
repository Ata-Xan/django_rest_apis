import requests

endpoint = "http://localhost:8001/api/"
# params ===> url/?arg=value ===> like here it is like: http://localhost:8001/api/?abc=123
get_response = requests.get(endpoint, params={"abc":123},json={"query": "Hello world"})
print(get_response.json()['message'])
print(get_response.status_code)
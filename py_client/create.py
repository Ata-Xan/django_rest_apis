import requests


endpoint = "http://localhost:8001/api/products/"
# params ===> url/?ar g=value ===> like here it is like: http://localhost:8001/api/?abc=123
data = {
    "title":"This field is done",
    "price":372.6
}
get_response = requests.post(endpoint, data)
print(get_response.json())

import requests


endpoint = "http://localhost:8001/api/products/1/update"
# params ===> url/?arg=value ===> like here it is like: http://localhost:8001/api/?abc=123
data ={
    "title":"Hello world my old friend",
    "price":12.99
}
get_response = requests.put(endpoint, data)


print(get_response.json())

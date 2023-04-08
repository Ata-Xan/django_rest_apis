import requests

product_id = input("Product id: \n")

try:
    product_id=int(product_id)
except:
    product_id = None
    print(f'{product_id} is not a valid id.')

if product_id:
    endpoint=f"http://localhost:8001/api/products/{product_id}/delete/"
# endpoint = "http://localhost:8001/api/products/"
# params ===> url/?arg=value ===> like here it is like: http://localhost:8001/api/?abc=123

get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code==204 )

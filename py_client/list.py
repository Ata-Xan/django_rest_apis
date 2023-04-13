import requests
from getpass import getpass
# list everything in the database
auth_endpoint = "http://localhost:8001/api/auth/"
username = input("What is your username? ")
password = getpass("What is your password? ")
# params ===> url/?arg=value ===> like here it is like: http://localhost:8001/api/?abc=123
auth_response = requests.post(auth_endpoint, json={'username': username, 'password':password})
print(auth_response.json())

if auth_response.status_code ==200:
    token = auth_response.json()['token']
    headers={
        # we can either put Bearer or Token if I want to use Bearer I need to have authenticaiton.py-like file in 
        # my api path.
        "Authorization":f"Bearer {token}"
    }
    endpoint="http://localhost:8001/api/products/"
    get_response=requests.get(endpoint, headers=headers)

    print(get_response.json())




# # list everything in the database
endpoint = "http://localhost:8001/api/products/"
# # params ===> url/?arg=value ===> like here it is like: http://localhost:8001/api/?abc=123
get_response = requests.get(endpoint)
print(get_response.json())

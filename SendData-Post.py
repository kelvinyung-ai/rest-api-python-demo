import requests
#import json

new_post = {
    "title": "Kelvin's Bootcamp Post",
    "body": "Learning REST APIs with Python!",
    "userId": 1
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)
print(response.status_code)
print(type(response))
print(response.json())

#Send the HTTP GET request
endpoint = 'https://httpbin.org/get'
response = requests.get(endpoint)

#Print out response JSON file
print(response.status_code)
data = response.json()
print("Response payload: ", data)
print(type(data))
print(type(response))
#python_obj= json.loads(response.tostring())
#print(type(python_obj))
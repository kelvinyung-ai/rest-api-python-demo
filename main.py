import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()
print(json.dumps(data, indent=2))
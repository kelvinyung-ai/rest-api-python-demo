import requests
import json

response1 = requests.get('https://jsonplaceholder.typicode.com/posts/1')
response2 = requests.get('https://jsonplaceholder.typicode.com/posts')
data1 = response1.json()
data2 = response2.json() 

for post in data1:
    print(type(post), type(data1))
    print('Key:', post, 'Value:', data1[post])

for post2 in data2[:5]:  # Print only the first 5 posts for brevity
    print(type(post2), type(data2))
    print('Post ID:', post2['id'], 'Title:', post2['title'])

#print(json.dumps(data, indent=2))
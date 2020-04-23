import requests

data = {'name': 'wenlinux', 'age': '25'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
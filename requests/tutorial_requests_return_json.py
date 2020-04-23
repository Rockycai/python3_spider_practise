import requests

r = requests.get('http://httpbin.org/get')
print(r.json())
print(type(r.json()))
print(r.json()['origin'])
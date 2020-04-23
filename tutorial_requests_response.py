import requests

r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.url)
print(r.history)
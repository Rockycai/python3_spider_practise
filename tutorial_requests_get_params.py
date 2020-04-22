import requests

r = requests.get('http://httpbin.org/get?name=wenlinux&age=25')
print(r.text)
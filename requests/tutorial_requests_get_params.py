import requests

data = {
    'name': 'wenlinux',
    'age': 25
}

#r = requests.get('http://httpbin.org/get?name=wenlinux&age=25')
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
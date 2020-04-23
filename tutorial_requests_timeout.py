import requests

try:
    r = requests.get('https://httpbin.org/get', timeout=1)
    print(r.status_code)
except requests.exceptions.ReadTimeout as e:
    print(e)

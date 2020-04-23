import requests

r = requests.get('http://httpbin.org/get')
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
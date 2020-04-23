import requests

proxies = {
    'http': 'http://111.112.113.114:8089',
    'https': 'http://111.112.113.115:8089',
}

# 需要身份认
#proxies = {'https': 'http://user:password@112.113.113.10:8089'}
requests.get('https://httpbin.org/get', proxies=proxies)
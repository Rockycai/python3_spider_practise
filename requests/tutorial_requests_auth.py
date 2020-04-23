import requests

r = requests.get('https://static3.scrape.cuiqingcai.com', auth=('admin', 'admin'))
print(r.status_code)
import requests
from requests.packages import urllib3
# ignore waring
urllib3.disable_warnings()

try:
    # 防止报SSLError错误
    response = requests.get('https://static2.scrape.cuiqingcai.com', verify=False)
    print(response.status_code)
except requests.exceptions.SSLError as e:
    print(e)
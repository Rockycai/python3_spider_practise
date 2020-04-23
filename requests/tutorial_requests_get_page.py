import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

r = requests.get('https://movie.douban.com/top250', headers=headers)
pattern = re.compile('<span class="title">([\u4e00-\u9fa5]*?)</span>')
titles = re.findall(pattern, r.text)
print(titles)
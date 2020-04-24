from pyquery import PyQuery as pq
doc = pq(url='https://www.wenlinux.com')
print(doc('title'))
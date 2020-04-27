# python3_spider_practise
python3 爬虫课代码

这是学习爬虫课程的总结，代码比较简单，个人是希望通过一些简单的使用，去举一反三，不仅有课程代码，个人也去做了一些小实验，比如爬取拉钩的top250名电影等。在提升个人技术的前提也去尝试一些有意思的事情

开发环境：python3.6.3, mac os X 10.13.6, vscode

## requests基本使用

安装**requests**

```bash
pip install requests
```

如果速度比较慢可以使用-i参数

```bash
pip install requests -i https://mirrors.aliyun.com/pypi/simple/
```

### requests用法

- get请求: [tutorial_requests_get.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_get.py)

- get带参数请求: [tutorial_requests_get.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_get.py)

- 解析json: [tutorial_requests_return_json.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_return_json.py)

- 爬豆瓣top250第一页电影名称: [tutorial_requests_get_page.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_get_page.py)

- 下载github ico图片: [tutorial_requests_get_bin.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_get_bin.py)

- post请求: [tutorial_requests_post.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_post.py)

- response信息: [tutorial_requests_response.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_response.py)

- 判断状态是否为200: [tutorial_requests_codes.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_codes.py)

- 上传文件: [tutorial_requests_upload_file.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_upload_file.py)

- 获取cookies: [tutorial_requests_cookies.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_cookies.py)

- 设置已经登陆cookies: [tutorial_requests_cookies_login.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_cookies_login.py)

- seesion维持: [tutorial_requests_session.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_session.py)

- 忽略不受信任的ssl: [tutorial_requests_ssl.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_ssl.py)

- 设置超时: [tutorial_requests_timeout.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_timeout.py)

- 身份认证: [tutorial_requests_auth.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_auth.py)

- 代理: [tutorial_requests_auth.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests/tutorial_requests_auth.py)

## pyquery基本使用

安装**pyquery**

```bash
pip install pyquery
```

如果速度比较慢可以使用-i参数

```bash
pip install pyquery -i https://mirrors.aliyun.com/pypi/simple/
```

pyquery 可以直接解析DOM节点的结构，并通过DOM节点的一些属性快速进行内容提取

### pyquery用法

- 字符串初始化: [tutorial_pyquery_string.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_string.py)

- url初始化: [tutorial_pyquery_url.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_url.py)

- 文件初始化: [tutorial_pyquery_file.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_file.py)

- css选择器用法: [tutorial_pyquery_css.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_css.py)

- 选择节点find用法: [tutorial_pyquery_find.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_find.py)

- 选择节点children用法: [tutorial_pyquery_children.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_children.py)

- 选择节点parent用法: [tutorial_pyquery_parent.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_parent.py)

- 返回祖先节点: [tutorial_pyquery_parents.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_parents.py)

- 返回兄弟节点: [tutorial_pyquery_siblings.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_siblings.py)

- 返回指定兄弟节点: [tutorial_pyquery_css_siblings.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_css_siblings.py)

- 获取属性 attr: [tutorial_pyquery_attr.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_attr.py)

- 遍历获取 attr: [tutorial_pyquery_items_attr.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_items_attr.py)

- 获取文本text: [tutorial_pyquery_text.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_text.py)

- 获取节点中的html: [tutorial_pyquery_html.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_html.py)

- 节点操作: [tutorial_pyquery_add_remove.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_add_remove.py)

- 移除节点: [tutorial_pyquery_remove.py](https://github.com/Rockycai/python3_spider_practise/blob/master/pyquery/tutorial_pyquery_remove.py)

## mongodb基本使用

安装**pymongo**

```bash
pip install pymongo 
```

如果速度比较慢可以使用-i参数

```bash
pip install pymongo -i https://mirrors.aliyun.com/pypi/simple/
```

### mongodb用法

- mongodb insert用法: [tutorial_mongodb_insert.py](https://github.com/Rockycai/python3_spider_practise/blob/master/mongodb/tutorial_mongodb_insert.py)

- mongodb insert_one: [tutorial_mongodb_insert_one.py](https://github.com/Rockycai/python3_spider_practise/blob/master/mongodb/tutorial_mongodb_insert_one.py)

- mongodb insert_many: [tutorial_mongodb_insert_many.py](https://github.com/Rockycai/python3_spider_practise/blob/master/mongodb/tutorial_mongodb_insert_many.py)

- mongodb find_one: [tutorial_mongodb_find_one.py](https://github.com/Rockycai/python3_spider_practise/blob/master/mongodb/tutorial_mongodb_find_one.py)

- mongodb operator: [tutorial_mongodb_operator.py](https://github.com/Rockycai/python3_spider_practise/blob/master/mongodb/tutorial_mongodb_operator.py)

## 案例1 requests pyquery mongodb 爬虫案例 

直接爬 https://static1.scrape.cuiqingcai.com 这个网址内容

- 用 requests 爬取这个站点每一页的电影列表，顺着列表再爬取每个电影的详情页。
- 用 pyquery 和正则表达式提取每部电影的名称、封面、类别、上映时间、评分、剧情简介等内容
- 把以上爬取的内容存入 MongoDB 数据库。
- 使用多进程实现爬取的加速。

1. 拿到页面内容
```python
def scrape_page(url):
    logging.info('scraping %s...', url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)
```

2. 通过拼接url给scrape_page函数，返回每一页的内容
```python
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)
```

3. 拿到详情页的链接拼成url
```python
def parse_index(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr.href
        detail_url = urljoin(BASE_URL, href)
        logging.info('get detail url %s', detail_url)
        yield detail_url
```
![url](https://github.com/Rockycai/python3_spider_practise/raw/master/images/1.png)

4. 通过选择器获取想要的内容
```python
def parse_detail(html):
    doc = pq(html)
    cover = doc('img.cover').attr.src
    name = doc('a > h2').text()
    categories = [item.text() for item in doc('.categories button span').items()]
    published_at = doc('.info:contains(上映)').text()
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
    drama = doc('.drama p').text()
    score = doc('p.score').text()
    score = float(score) if score else None
    
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }
```

分析
- 封面：是一个 img 节点，其 class 属性为 cover。
- 名称：是一个 h2 节点，其内容便是名称。
- 类别：是 span 节点，其内容便是类别内容，其外侧是 button 节点，再外侧则是 class 为 categories 的 div 节点。
- 上映时间：是 span 节点，其内容包含了上映时间，其外侧是包含了 class 为 info 的 div 节点。但注意这个 div 前面还有一个 class 为 info 的 div 节点，我们可以使用其内容来区分，也可以使用 nth-child 或 nth-of-type 这样的选择器来区分。另外提取结果中还多了「上映」二字，我们可以用正则表达式把日期提取出来。
- 评分：是一个 p 节点，其内容便是评分，p 节点的 class 属性为 score。
- 剧情简介：是一个 p 节点，其内容便是剧情简介，其外侧是 class 为 drama 的 div 节点。

5. 写入mongodb, $set如果没有则新建,否则就修改
```python
def save_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    },  upsert=True)
```

6. 启用多进程, 加快爬虫速度
```python
if __name__ == '__main__':
    pool = multiprocessing.Pool() 
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()
    pool.join()
```

[requests_pyquery_mongodb_spider.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests_pyquery_mongodb_spider.py)

## 案例2 爬豆瓣250名的电影名称，分类等信息

- 由于豆瓣官网的验证需要加入headers
- 豆瓣也会对频繁的ip进行限制，所以要搭建代理池工具

使用代理工具：[proxy_pool](https://github.com/jhao104/proxy_pool)

```python
# 获取一个代理ip和端口，这是利用proxy_pool的api
def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
```

通过代理，返回页面的内容
```python
def scrape_page(url, page, data={}):
    retry_count = 3
    logging.info('scraping %s...', url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    while retry_count > 0:
        proxy = get_proxy().get("proxy")
        try:
            if data:
                response = requests.get(url, headers=headers, params=data, proxies={"http": "http://{}".format(proxy)})
            else:
                response = requests.get(url, headers=headers, proxies={"http": "http://{}".format(proxy)})
            if response.status_code == 200:
                return response.text
            logging.error('get invalid status code %s while scraping %s', response.status_code, url)
        except requests.RequestException:
            retry_count -= 1
            logging.error('error occurred while scraping %s', url, exc_info=True)
    delete_proxy(proxy)
```

获取详情页url
```python
def parse_index(html):
    doc = pq(html)
    links = doc('.grid_view .item .pic a')
    for link in links.items():
        href = link.attr.href
        logging.info('get detail url %s', href)
        yield href
```

爬详情页所需要的内容
```python
def scrap_detail(html):
    doc = pq(html)
    title = doc('h1 span').text()
    img = doc('#mainpic img').attr.src
    categories = [ item.text() for item in doc('#info span[property="v:genre"]').items()]
    contents = doc('#link-report span[property="v:summary"]').text()
    release_dates = [ item.text() for item in doc('#info span[property="v:initialReleaseDate"]').items()]
    score = doc('.rating_self strong[property="v:average"]').text()

    return {
        'title': title,
        'img': img,
        'categories': categories,
        'contents': contents,
        'release_dates': release_dates,
        'score': score
    }
```

写入mongodb
```python
def main(pages):
    for page in range(pages):
        data = {
            'start': page * 25,
            'filter': None
        }
        html = scrape_page(BASE_URL, page, data)
        for index in parse_index(html):
            detail_html = scrape_page(index, page)
            data = scrap_detail(detail_html)
            logging.info('get detail data %s', data)
            logging.info('saving data to mongodb')
            save_data(data)
            logging.info('data saved successfully')
```

多进程爬虫加快效率
```python
if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(0, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()
    pool.join()
```

[requests_pyquery_mongodb_douban.py](https://github.com/Rockycai/python3_spider_practise/blob/master/requests_pyquery_mongodb_douban.py)
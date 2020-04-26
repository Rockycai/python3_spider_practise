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

## requests pyquery mongodb 爬虫案例

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
    return scrape_page(index_url
```
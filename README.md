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

- get请求: [tutorial_requests_get.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_get.py)

- get带参数请求: [tutorial_requests_get.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_get.py)

- 解析json: [tutorial_requests_return_json.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_return_json.py)

- 爬豆瓣top250第一页电影名称: [tutorial_requests_get_page.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_get_page.py)

- 下载github ico图片: [tutorial_requests_get_bin.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_get_bin.py)

- post请求: [tutorial_requests_post.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_post.py)

- response信息: [tutorial_requests_response.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_response.py)

- 判断状态是否为200: [tutorial_requests_codes.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_codes.py)

- 上传文件: [tutorial_requests_upload_file.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_upload_file.py)

- 获取cookies: [tutorial_requests_cookies.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_cookies.py)

- 设置已经登陆cookies: [tutorial_requests_cookies_login.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_cookies_login.py)

- seesion维持: [tutorial_requests_session.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_session.py)

- 忽略不受信任的ssl: [tutorial_requests_ssl.py](https://github.com/Rockycai/python3_spider_practise/blob/master/tutorial_requests_ssl.py)
import requests
import logging
import re
import pymongo
import multiprocessing
from pyquery import PyQuery as pq
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://movie.douban.com/top250'
TOTAL_PAGE = 10


MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'top_movies'
MONGO_COLLECTION_NAME = 'top_movies'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['top_movies']
collection = db['top_movies']

def save_data(data):
    collection.update_one({
        'title': data.get('title')
    }, {
        '$set': data
    },  upsert=True)

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


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

def parse_index(html):
    doc = pq(html)
    links = doc('.grid_view .item .pic a')
    for link in links.items():
        href = link.attr.href
        logging.info('get detail url %s', href)
        yield href

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


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(0, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()
    pool.join()
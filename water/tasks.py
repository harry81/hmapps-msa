# -*- coding: utf-8 -*-
from water.utils import (fetch_news_to_S3,
                         load_from_S3,
                         send_email_for_fetched_articles,
                         insert_news_to_db,
                         load_cafe_article)


def celery_test(self,  **kwargs):
    pass


def celery_send_email_for_fetched_articles(self,  **kwargs):
    # {"url": "http://file.mk.co.kr/news/rss/rss_30100041.xml"}
    # {"url": "http://www.hani.co.kr/rss/"}
    urls = kwargs.get('url', None)

    if not isinstance(urls, list):
        urls = urls,

    for url in urls:
        fetch_news_to_S3(url=url)
        articles = load_from_S3(url=url)
        insert_news_to_db(articles)

    send_email_for_fetched_articles(articles)


def event_send_email_for_fetched_articles():
    urls = ["http://file.mk.co.kr/news/rss/rss_30100041.xml",]
    # {"url": "http://file.mk.co.kr/news/rss/rss_30100041.xml"}
    # {"url": "http://www.hani.co.kr/rss/"}

    if not isinstance(urls, list):
        urls = urls,

    for url in urls:
        fetch_news_to_S3(url=url)
        articles = load_from_S3(url=url)
        insert_news_to_db(articles)

    send_email_for_fetched_articles(articles)


def celery_load_cafe_article(self):
    load_cafe_article()

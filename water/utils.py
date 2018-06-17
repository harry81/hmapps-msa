import json
from datetime import datetime
from io import BytesIO
from urllib.parse import urlparse

import requests
from dateutil.parser import parse as parse
from django.core.files.storage import default_storage
from django.core.mail import EmailMultiAlternatives
from django.db import IntegrityError
from konlpy.tag import Hannanum
from konlpy.utils import pprint
from naver_api.naver_search import Naver

from lxml import etree

from .models import Article, Item

naver = Naver()

hannanum = Hannanum()


def _get_filename(item=None):

    if item is None:
        return None

    url = item.xpath('link/text()')[0]
    published = parse(item.xpath('pubDate/text()')[0])

    if 'hani.co.kr' in url:
        category = 'hani'
        filename = '%s/%s-%s' % (category,
                                 published.strftime('%Y-%m-%d'),
                                 urlparse(url).path.split('/')[-1])

    elif 'mk.co.kr' in url:
        category = 'mk'
        filename = '%s/%s-%s.html' % (
            category,
            published.strftime('%Y-%m-%d'),
            urlparse(url).query.split('&')[0].split('=')[1])

    return filename, category


def fetch_news_to_S3(url='http://www.hani.co.kr/rss/'):
    feeds = requests.get(url)
    output = BytesIO(feeds.content)

    try:
        tree = etree.parse(output)
    except etree.XMLSyntaxError:
        tree = etree.parse(output, etree.XMLParser(encoding='utf-8'))

    for item in tree.xpath('/rss/channel/item'):
        filename, category = _get_filename(item)
        url = item.xpath('link/text()')[0]

        if default_storage.exists(filename):
            print ('Skiped because already done - %s' % filename)
            continue

        rep = requests.get(url)

        fp = default_storage.open('%s' % (filename), 'w')
        fp.write(rep.content)
        fp.close()


def load_from_S3(url='http://www.hani.co.kr/rss/'):
    articles = []
    prefix = _get_prefix(url)

    for ele in default_storage.bucket.list(
            prefix='%s/%s' % (prefix, datetime.now().strftime('%Y-%m-%d'))):

        article = eval('_parse_%s' % prefix)(ele)

        if article:
            articles.append(article)
    return articles


def send_email_for_fetched_articles(articles):
    subject = '%s - Daily News' % datetime.now().strftime('%Y-%m-%d')
    from_email, to = 'chharry@gmail.com', 'chharry@gmail.com'
    text_content = ''
    html_content = ''

    for article in articles:
        html_content += "<p><a href='%s'>%s</a></p>" % (
            article['url'], article['title'])

        text_content += "%s - %s" % (
            article['title'], article['url'],)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def _get_prefix(url):
    if 'mk' in url:
        return 'mk'
    else:
        return 'hani'


def insert_news_to_db(articles):
    for article in articles:
        try:
            item, created = Item.objects.update_or_create(url=article['url'], defaults=article)
            print (item, created)
        except:
            print ("Problem in Inserting")


def _parse_hani(ele):
    content = ele.read()
    root = etree.HTML(content)
    article = {'publisher': 'h'}

    try:
        article['url'] = root.xpath(
            '//meta[@property="og:url"]/@content')[0]
        article['title'] = root.xpath('//title/text()')[0].replace(u' : 뉴스 : 한겨레', '')

        subtitle = root.xpath('//div[@class="subtitle"]/text()')
        subtitle = '\n'.join(map(lambda x: x.strip(), subtitle))

        article['subtitle'] = subtitle

        text = root.xpath('//div[@class="text"]/text()')
        if len(text) == 0:
            text = root.xpath('//div[@class="article-contents"]/text()')

        text = '\n'.join(map(lambda x: x.strip(), text)).strip()
        article['text'] = text

        try:
            publish_at = root.xpath('//p[@class="date-time"]/span/text()')

        except ValueError:
            publish_at = root.xpath('//p[@class="date"]/span/text()')

        article['publish_at'] = datetime.strptime(publish_at[0], '%Y-%m-%d %H:%M')
        article['imgs'] = root.xpath('//div[@class="image"]/img/@src')

    except IndexError as e:
        print (e)

    return article


def _parse_mk(ele):
    content = ele.read()
    root = etree.HTML(content)
    article = {'publisher': 'm'}

    try:
        article['url'] = root.xpath(
            '//meta[@property="og:url"]/@content')[0]
        article['title'] = root.xpath('//title/text()')[0].replace('MK News - ', '')
        article['subtitle'] = '\n'.join(root.xpath('//h2[@class="sub_title1"]/text()'))

        text = root.xpath("//div[@class='art_txt']/text()")

        if len(text) == 0:
            text = root.xpath('//div[@class="article-contents"]/text()')

        text = '\n'.join(map(lambda x: x.strip(), text)).strip()
        article['text'] = text

        publish_at = root.xpath('//li[@class="lasttime"]/text()')[0].split(':', 1)[1].strip()
        article['publish_at'] = datetime.strptime(publish_at, '%Y.%m.%d %H:%M:%S')
        article['imgs'] = root.xpath('//div[@class="img_center"]/img/@src')

    except UnicodeEncodeError as e:
        print (e)
        return

    except IndexError as e:
        print (e)
        return

    return article


def load_cafe_article():
    """
    주기 : 1분
    작업 : 네이버 카페글의 타이틀을 s3에 저장한다
    """
    rows = naver.search()
    title = rows[0].get("title")
    created_at = rows[0].get("created_at")
    filename = "%s/%s.%s" % ('articles',
                             datetime.now().strftime("%Y%m%d/%H%M%S"), "json")

    fp = default_storage.open('%s' % (filename), 'w')
    fp.write(json.dumps(rows))
    fp.close()

    print("%s : %s" % (created_at, title))


def fetch_article():
    """
    주기 : 하루
    작업 : s3에 저장된 글을 테이블에 저장한다.
    """
    dir_name = 'articles/%s/' % datetime.now().strftime("%Y%m%d")

    for ele in default_storage.listdir(dir_name)[1]:
        full_path = dir_name + ele
        default_storage.exists(full_path)
        fp = default_storage.open(full_path, 'r')

        content = fp.read()
        rows = json.loads(content)

        try:
            Article.objects.bulk_create([Article(**row) for row in rows])
        except IntegrityError:
            pass


def tag_article():
    """
    주기 : 하루
    작업 : 게시물의 명사를 기준으로 테그한다.
    """
    for article in Article.objects.all():
        try:
            article.do_tag([tag for tag in hannanum.nouns(article.title) if len(tag) > 1])
        except Exception as e:
            print(hannanum.nouns(article.title))
            print(e)

import random
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from pws import Bing
from pws.google import strip_tags


def main():
    # c = gnp_fixed.get_google_news_query("earth")
    # print(c)
    # return

    # cnn_paper = newspaper.build('http://cnn.com/search/?q=trump')
    r = Bing.search_news(10, 0, True, 'h', query='github')
    print(r)
    return

    for article in cnn_paper.articles:
        print(article.url)
        if "trump" in str(article).lower():
            article.download()
            article.parse()
            article.nlp()
            print(article.summary)
            break


def get_articles_testing(topic, start, end):
    return [get_article_testing() for x in range(0, 100)]


def generate_news_url(query, num, start, recent, country_code):
    query = '+'.join(query.split())
    url = 'https://www.google.com/search?q=' + query + '&num=' + num + '&start=' + start
    url += '&tbm=nws#q=' + query + '&tbas=0&tbs=sbd:1&tbm=nws'
    if recent in ['h', 'd', 'w', 'm', 'y']:
        url += '&tbs=qdr:' + recent
    if country_code is not None:
        url += '&gl=' + country_code
    return url


def get_info(i):
    pass


def convert_to_epoch_time(param):
    time_ago = [int(s) for s in param.split(" ") if s.isdigit()][0]

    if "second" in param:
        multiplier = 1
    elif "minute" in param:
        multiplier = 60
    elif "hour" in param:
        multiplier = 60 * 60
    elif "day" in param:
        multiplier = 60 * 60 * 24
    elif "week" in param:
        multiplier = 60 * 60 * 24 * 7
    elif "month" in param:
        multiplier = 60 * 60 * 24 * 30
    elif "year" in param:
        multiplier = 60 * 60 * 24 * 365.25
    else:
        try:
            pattern = '%d %b %Y'
            return int(time.mktime(time.strptime(param, pattern)))
        except Exception as e:
            print(e)
        raise Exception("Unexpected time duration! {}".format(str(param)))
    seconds_ago = multiplier * time_ago
    now_epoch_time = int(time.time())
    return now_epoch_time - seconds_ago


def scrape_news_result(soup):
    raw_results = soup.find_all('div', attrs={'class': 'g'})
    results = []

    for result in raw_results:
        link = result.find('a').get('href')[7:]

        raw_link_text = result.find('a')
        link_text = strip_tags(str(raw_link_text))

        raw_link_info = result.find('div', attrs={'class': 'st'})
        link_info = strip_tags(str(raw_link_info))

        raw_source = result.find('span', attrs={'class': 'f'})
        raw_source = strip_tags(str(raw_source)).split(' - ')

        source = raw_source[0]
        time = convert_to_epoch_time(raw_source[1])

        additional_links = dict()

        # Crazy hack! Fix it. + Buggy!
        try:
            raw_a_links = result.find_all('a')[1:]
            if raw_a_links:
                raw_source = list(map(strip_tags, list(map(str, result.find_all('span', attrs={'class': 'f'})[1:]))))
                for idx in range(len(raw_a_links) - 1):
                    additional_links[strip_tags(str(raw_a_links[idx]))] = (
                        raw_a_links[idx].get('href'), raw_source[idx])
        except Exception as e:
            print(e)

        temp = {'link': link,
                'link_text': link_text,
                'link_info': link_info,
                'additional_links': additional_links,
                'source': source,
                'time': time,
                }
        results.append(temp)
    return results


def search_news(query, num=10, start=0, recent=None, country_code=None):
    url = generate_news_url(query, str(num), str(start), country_code, recent)
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    results = scrape_news_result(soup)

    # raw_total_results = soup.find('div', attrs={'class': 'sd'}).string
    # total_results = int(str(raw_total_results).replace(",","").replace("About ","").replace(" results","").strip())
    temp = {'results': results,
            'url': url,
            'num': num,
            'start': start,
            'search_engine': 'google',
            'total_results': 0,
            'country_code': country_code,
            }
    return temp


def getKey(item):
    return item["time"]


def get_articles(topic, start, end, skipNum):
    r = search_news(str(topic), 10, skipNum)
    return sorted(r["results"], key=getKey, reverse=True)


def get_random_date():
    year = random.choice(range(1950, 2001))
    month = random.choice(range(1, 13))
    day = random.choice(range(1, 29))
    birth_date = datetime(year, month, day)
    return str(birth_date)


def get_article_testing():
    return {
        "date": get_random_date(),
        "summary": "something something something something something something something something ",
        "title": "donnald trump is elected",
        "source": "fake.news",
        "isimage": "false"
    }


if __name__ == "__main__":
    start = "1232131"
    end = "1232131"
    r = get_articles("slack", start, end, 0)
    for i in r:
        print(i["time"])
    pass

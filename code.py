from bs4 import BeautifulSoup
import requests as rq

toi = rq.get("https://timesofindia.indiatimes.com/rss.cms")
toi_soup = BeautifulSoup(toi.text, 'html.parser')

rss_anchors = toi_soup.find_all("a", "rssurl" )

for rss_link in rss_anchors:
    xml_link = rss_link.get('href')
    xml_soup = BeautifulSoup(rq.get(xml_link).text, 'html.parser')
    title = xml_soup.find_all("title")
    try:
        print(title[2].string)
    except IndexError:
        pass
        
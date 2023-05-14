import requests
import logging
from lxml import html


def get_html_content(url):
    # Disable logging for the "requests" library
    logging.getLogger("requests").setLevel(logging.WARNING)

    # Disable logging for the "urllib3" library
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    # Disable logging for the "lxml" library
    logging.getLogger("lxml").setLevel(logging.WARNING)
    return requests.get(url).text
    

def parse_html_to_xmltree(html_content):
    return html.fromstring(html_content)


class MediaContentCreator:
    def __init__(self, url, news_container_xpath, title_container_xpath, date_container_xpath):
        self.url = url
        self.news_container_xpath = news_container_xpath
        self.news_title_xpath = title_container_xpath
        self.news_date_xpath = date_container_xpath


    def set_xpath_to_news_container(self, xpath):
        self.news_container_xpath = xpath


    def set_xpath_to_title(self, xpath):
            self.news_title_xpath = xpath


    def set_xpath_to_date(self, xpath):
            self.news_date_xpath = xpath


    def get_latest_news(self):  # this function will return an array of the latest news available
        html_content = get_html_content(self.url)
        xml_tree = parse_html_to_xmltree(html_content)
        latest_news = xml_tree.xpath(self.news_container_xpath)

        articles = []
        for article in latest_news:
            title = article.xpath(self.news_title_xpath)[0].text

            date = 'Today'
            if not self.news_date_xpath is None:
                date = article.xpath(self.news_date_xpath)[0].text

            articles.append([{"date": date, "title": title}])
        
        return articles

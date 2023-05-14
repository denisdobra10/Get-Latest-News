from media_content_creator import MediaContentCreator
import json
import os

def get_protv_latest_articles():
    url = 'https://stirileprotv.ro/'
    news_container_xpath = '//div[@class="latest-items"]/*[@class="item"]'
    title_container_xpath = './/*[@class="item-article_title"]'
    date_container_xpath = './/*[@class="date"]'
    
    return MediaContentCreator(url, news_container_xpath, title_container_xpath, date_container_xpath).get_latest_news()


def get_mediafax_latest_articles():
    url = 'https://www.mediafax.ro/'
    news_container_xpath = '//div[@class="BreakingNews"]/ul/li'
    title_container_xpath = './/p/*[@class="title"]'
    date_container_xpath = None

    return MediaContentCreator(url, news_container_xpath, title_container_xpath, date_container_xpath).get_latest_news()


def get_digi_latest_articles():
    url = 'https://www.digi24.ro/stiri'
    news_container_xpath = '//div[@class="article-content"]'
    title_container_xpath = './/h2/a'
    date_container_xpath = None
    
    return MediaContentCreator(url, news_container_xpath, title_container_xpath, date_container_xpath).get_latest_news()


def get_articles_from_creators():
    latest_articles = []
    latest_articles.append({"creator": "Digi", "news": get_digi_latest_articles()})
    latest_articles.append({"creator": "ProTV", "news": get_protv_latest_articles()})
    latest_articles.append({"creator": "Mediafax", "news": get_mediafax_latest_articles()})

    return latest_articles


def save_news_on_disk(news):
    output_filename = 'news_output.json'
    cwd = os.getcwd()
    output_path = os.path.join(cwd, output_filename)

    with open(output_path, 'w') as f:
        json.dump(news, f)


def main():
    news = get_articles_from_creators()
    
    save_news_on_disk(news)
    print("Un fisier output cu toate stirile a fost salvat in directorul fisierului!")
    if 'nu' in input("Vrei sa citesti cele mai noi stiri de azi? (da/nu): ").lower():
        return

    i = 1
    for source in news:
        creator = source['creator']
        articles = source['news']

        for article_list in articles:
            for article in article_list:
                title = article['title']
                date = article['date']
                print(f'Articolul {i} -- Creator: {creator} -> Titlu: {title} Data: {date}')
                i += 1

                if 'nu' in input("Doresti sa citesti urmatorul articol? (da/nu): ").lower():
                    return
                
    print("Ai finalizat stirile de azi! Revino maine pentru mai multe noutati")


main()

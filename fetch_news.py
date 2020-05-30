import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()

from django.conf import settings

from news.models import News

import requests

# Welcome to the king of all spaghetti code. Goodluck!
def get_news_articles(endpoint):
    '''
    Fetches news articles from NEWSAPI.ORG and saves them as `News` objects
    '''
    r = requests.get(endpoint)

    jsonResponse = r.json()
    articles = jsonResponse['articles']

    for i in articles:
        
        # Get source
        source_dict = i.get('source')
        source_name = source_dict.get('name')

        if source_name == None:
            name = 'latest headlines'

        else:
            name = source_name

        # get author
        author = i.get('author')

        if not author == None:

            # get title
            title = i.get('title')

            if not title == None:

                # description
                description = i.get('description')

                if not description == None:

                    # get url
                    url = i.get('url')

                    if not url == None:

                        # get image url
                        urlToImage = i.get('urlToImage')

                        if not urlToImage == None:

                            # get date published
                            publishedAt = i.get('publishedAt')

                            try:
                                obj = News.objects.get(url=url)
                                pass

                            except:
                                News.objects.create(
                                    source=name,
                                    author=author,
                                    title=title,
                                    content=description,
                                    url=url,
                                    urlToImage=urlToImage,
                                    publishedAt=publishedAt
                                )

                                print('Articles Saved')

                        else:
                            pass

                    else:
                        pass

                else:
                    pass

            else:
                pass

        else:
            pass




apiKey = 'db01c2e94fdd4698acc4dc6cc68a50e2'

# ENDPOINTS
endpoint = f'http://newsapi.org/v2/top-headlines?language=en&sortBy=publishedAt&apiKey={apiKey}'

get_news_articles(endpoint)
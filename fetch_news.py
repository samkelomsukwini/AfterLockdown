import os
import random
import string

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()

from django.conf import settings

from news.models import News

import requests



def post_call_id_generator(size=10, chars=string.ascii_letters + string.digits):
    '''
    Generates and returns `Submission` base64 call id
    '''
    return ''.join(random.choice(chars) for _ in range(size))


def check_call_id_exists(call_id):
    '''
    Checks if call id exists. Generates and returns new call id if exists
    '''
    # Try/Catch checks to see if a Submission with call_id == call_id
    # already exists. This will not throw an error if True. And if
    # that's the case, the function becomes recursive until a unique
    # call_id is generated
    try:
        News.objects.get(call_id=call_id)

        # New call_id generated
        new_call_id = post_call_id_generator()

        # New call_id checked against all Submission objects
        check_call_id_exists(new_call_id)
    
    except:
        # This means there has been an error which means
        # that there's no Submission object with call_id == call_id
        return call_id

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
                                # generate call_id
                                _call_id = post_call_id_generator()

                                # Check to see if generated call_id exists in DB
                                call_id = check_call_id_exists(_call_id)

                                News.objects.create(
                                    call_id=call_id,
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
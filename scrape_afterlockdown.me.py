import os
import random
import string

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()

from django.conf import settings

import requests

from bs4 import BeautifulSoup

from afterlockdown.models import Post


site = requests.get('https://afterlockdown.me/')

soup = BeautifulSoup(site.text, 'lxml')

posts = soup.find_all(class_='card')


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
        Post.objects.get(call_id=call_id)

        # New call_id generated
        new_call_id = post_call_id_generator()

        # New call_id checked against all Submission objects
        check_call_id_exists(new_call_id)
    
    except:
        # This means there has been an error which means
        # that there's no Submission object with call_id == call_id
        return call_id


for i in posts:
    messages = i.find(class_='card__message').get_text()
    cities = i.find(class_='card__location').get_text()

    print(cities)

    _call_id = post_call_id_generator()
    call_id = check_call_id_exists(_call_id)

    Post.objects.create(city=cities, body=messages, call_id=call_id)
import os
import random
import string

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()

from django.conf import settings

import tweepy

from afterlockdown.models import Post


auth = tweepy.OAuthHandler('foLrwYNAr3Vhru873F9KDIgzC', 'wT5txGO8vx3ODimsnYAZLdRrt15YvDkmjqe50uPY9L1iRaoTdx')
auth.set_access_token('1265214128051892226-s17SqFTBnmQ8OOjqQQdepD5YmvISXp', 'bvK7dkQb2a1Th4oaOoYh8yS4GUrYwfscIFt0RldMT3EoZ')

api = tweepy.API(auth)

post = Post.objects.order_by('?').first()


public_tweets = api.update_status(status=f'{post.body} http://samkelo.me/s/{post.call_id} #lockdown #covid19', place_id='Ekhaya LamaSukwini')

print('Done')

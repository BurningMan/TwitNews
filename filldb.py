import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from django.db import models
from homepage.models import Tweet 
import twitt 


def fillCategory(catg):
    timeline = twitt.get_tweets()
    for tweet in timeline:
            Tweet.objects.create(text=tweet.text.encode('utf-8'),
                author=tweet.user.name.encode('utf-8'),
                category=catg,
                datetime='Today',
                avatar=tweet.user.profile_image_url)


if __name__ == "__main__":
    fillCategory('it')

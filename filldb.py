import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.conf import settings
from django.db import models
from homepage.models import Tweet 
import twitter 


def fillCategory(catg):
    timeline = twitter.get_tweets()
    for i in timeline:
            Tweet.objects.create(text=i.text.encode('utf-8'),
                author=i.user.name.encode('utf-8'),
                category=catg,
                datetime = 'Today',
                avatar=i.user.profile_image_url)


if __name__ == "__main__":
    fillCategory('it')

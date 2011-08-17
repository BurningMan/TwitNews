import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from django.db import models
from homepage.models import Tweet
import twitter_search


def fillCategory(catg):
    timeline = twitter_search.search_tweets(catg,result_type="recent")
    for tweet in timeline:
            Tweet.objects.create(text=tweet.text.encode('utf-8'),
                author=tweet.from_user.encode('utf-8'),
                category=catg,
                datetime='Today',
                avatar=tweet.profile_image_url)


if __name__ == "__main__":
    fillCategory('it')

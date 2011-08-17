import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from django.db import models
from homepage.models import Tweet
import twitter_search

def updateCategory(catg):
    tweetObjects = Tweet.objects.filter(category=catg)
    if tweetObjects.count():
        timeline = twitter_search.search_tweets(catg,result_type="recent")
        j = 0

        for tweet in timeline:

            t = tweetObjects[j]
            t.text = tweet.text.encode('utf-8')
            t.author = tweet.from_user.encode('utf-8')
            t.category = catg
            t.datetime = 'Today'
            t.avatar = tweet.profile_image_url
            t.save()

            j = j + 1



if __name__ == "__main__":
    updateCategory('it')

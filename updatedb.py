import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.conf import settings
from django.db import models
from homepage.models import Tweet 
import twitter 

def updateCategory(catg):
    tweetObjects = Tweet.objects.filter(category=catg)
    if tweetObjects.count() > 0:
        timeline = twitter.get_tweets()
        j = 0

        for i in timeline:

            t = tweetObjects[j]
            t.text = i.text.encode('utf-8')
            t.author = i.user.name.encode('utf-8')
            t.category = catg
            t.datetime = 'Today'
            t.avatar = i.user.profile_image_url
            t.save()

            j = j + 1



if __name__ == "__main__":
    updateCategory('it')

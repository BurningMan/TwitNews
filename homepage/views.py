# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from homepage.models import Tweet
import twitter 

def homepage(request):
    tweetObjects = Tweet.objects.all()
    tweets = []
    i = 1
    for t in tweetObjects:
        tweets.append([i, t])
        i = i + 1
    return render_to_response('index.html', {'tweets': tweets})

# Fill database (default data)
def fillDatabase(request):
    timeline = twitter.get_tweets()
    for i in timeline:
        Tweet.objects.create(text=i.text.encode('utf-8'),
            author=i.user.name.encode('utf-8'),
            category='IT',
            datetime = 'Today',
            avatar=i.user.profile_image_url)
    return render_to_response('filldb.html', )



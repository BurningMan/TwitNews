# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from tnews.models import Tweet

def homepage(request):
    tweetObjects = Tweet.objects.all()
    tweets = []
    i = 1
    for t in tweetObjects:
        tweets.append([i, t])
        i = i + 1
    return render_to_response('index.html', {'tweets': tweets})

def categories(request):
    return render_to_response('categories.html', )

# Fill database (default data)
def fillDatabase(request):
    for i in range(1, 16):
        Tweet.objects.create(text='Text of tweet',
            author='Author of tweet',
            category='IT',
            datetime = 'Today',
            avatar='http://a3.twimg.com/profile_images/1232871818/danicon_normal.png')
    return render_to_response('filldb.html', )



# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from homepage.models import Tweet

def homepage(request):
    tweetObjects = Tweet.objects.filter(category='it')
    tweets = []
    i = 1
    for t in tweetObjects:
        tweets.append([i, t])
        i = i + 1
    return render_to_response('base_tweets.html', {'tweets': tweets,'category': '','title': 'Home'})

def categories(request):
    return render_to_response('categories.html', )

def tweetsByCategory(request, catg):
    tweetObjects = Tweet.objects.filter(category=catg)
    if tweetObjects.count() > 0:
        tweets = []
        i = 1
        for t in tweetObjects:
            tweets.append([i, t])
            i = i + 1
        return render_to_response('base_tweets.html', {'tweets': tweets,'category': catg.upper(),'title': catg})
    else: 
        return render_to_response('pageNotFound.html', )

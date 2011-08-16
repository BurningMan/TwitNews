# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from homepage.models import Tweet

def homepage(request):
    tweetObjects = Tweet.objects.filter(category='it')
    tweets = []
    i = 1
    for tweet in tweetObjects:
        tweets.append([i, tweet])
        i = i + 1
    return render_to_response('base_tweets.html', 
        RequestContext(request, {'tweets': tweets, 'category': '', 'title': 'Home'}))


def categories(request):
    return render_to_response('categories.html', RequestContext(request, ))


def tweetsByCategory(request, category):
    tweetObjects = Tweet.objects.filter(category=category)
    if tweetObjects.count():
        tweets = []
        i = 1
        for tweet in tweetObjects:
            tweets.append([i, tweet])
            i = i + 1
        return render_to_response('base_tweets.html', 
                RequestContext(request, 
                    {'tweets': tweets, 'category': category.upper(), 'title': category}))
    else: 
        raise Http404

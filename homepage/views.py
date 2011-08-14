# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from homepage.models import Tweet
import twitter 

def homepage(request):
    tweetObjects = Tweet.objects.filter(category='it')
    tweets = []
    i = 1
    for t in tweetObjects:
        tweets.append([i, t])
        i = i + 1
    return render_to_response('index.html', {'tweets': tweets})

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
        return render_to_response('{0}.html'.format(catg), {'tweets': tweets})
    else: 
        return render_to_response('pageNotFound.html', )

######################################################################

# Fill database (default data)
def fillCategory(request, catg):
    timeline = twitter.get_tweets()
    for i in timeline:
        Tweet.objects.create(text=i.text.encode('utf-8'),
            author=i.user.name.encode('utf-8'),
            category=catg,
            datetime = 'Today',
            avatar=i.user.profile_image_url)
    return render_to_response('filldb.html', )
######################################################################
def updateDatabase(request, catg):
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

        return render_to_response('filldb.html', )
    else: 
        return render_to_response('pageNotFound.html', )

######################################################################

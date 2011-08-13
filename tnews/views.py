# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from tnews.models import Tweet
import twitter 

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



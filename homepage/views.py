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

#!/usr/bin/env python

import os
import simplejson
import urllib
import urllib2

class Status:
    def __init__(self,created_at,profile_image_url,from_user_id_str,id_str,from_user,text,to_user_id,id,geo,from_user_id,source,to_user_id_str,recent_retweets="null"):
        self.created_at=created_at
        self.profile_image_url=profile_image_url
        self.from_user_id_str=from_user_id_str
        self.id_str=id_str
        self.from_user=from_user
        self.text=text
        self.to_user_id=to_user_id
        self.id=id
        self.geo=geo
        self.from_user_id=from_user_id
        self.source=source
        self.to_user_id_str=to_user_id_str
        self.recent_retweets=recent_retweets

def parse(page):
    tweets=[]
    search=simplejson.loads(page)
    results=search["results"]
    for i in results:
        tmp=Status(i["created_at"],
        i["profile_image_url"],
        i["from_user_id_str"],
        i["id_str"],
        i["from_user"],
        i["text"],
        i["to_user_id"],
        i["id"],
        i["geo"],
        i["from_user_id"],
        i["source"],
        i["to_user_id_str"]
        )
        if i["metadata"]["result_type"]=='popular':
            tmp.recent_retweets=i["metadata"]["recent_retweets"]
        tweets.append(tmp)
    return tweets
def search_tweets(q,geocode="",lang="",result_type="mixed",show_user=False,until="",since_id=""):
    url="http://search.twitter.com/search.json"
    values={'q':q,
    'result_type':result_type
    }
    data=urllib.urlencode(values)
    req=urllib2.Request(url,data)
    response=urllib2.urlopen(req)
    page=response.read()
    return parse(page)

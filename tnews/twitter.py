#-------------------------------------------------------------------------------
# Name:        ??????1
# Purpose:
#
# Author:      Dark
#
# Created:     12.08.2011
# Copyright:   (c) Dark 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os
import tweepy
def get_tweets():
    CONSUMER_KEY="uFZ2vP6MxiaoE3tMX5pguFZ2vP6MxiaoE3tMX5pg"
    CONSUMER_SECRET="yeguaZCwIDloZ3MNs3XUV30vRAlvPq8qjVMrUFIgzxg"
    ACCESS_KEY="82398613-5EvSnXi8ZY2Sl852c5xGf7gfUqFUqR6KKvgph0GI"
    ACCESS_SECRET="4qrFxb6rjEzptOpfK8hFeZYrsSScI625XWdo3oQ17VE"
    auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
    api=tweepy.API(auth)
    timeline=api.public_timeline()
    for i in timeline:
        print i.text.encode('utf-8')
        print i.user.name.encode('utf-8')
        print i.user.profile_image_url
    return timeline

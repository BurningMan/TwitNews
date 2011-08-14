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
import ConfigParser
def get_tweets():
    config=ConfigParser.ConfigParser()
    config.read('twitter.cfg')
    CONSUMER_KEY=config.get('main','CONSUMER_KEY')
    CONSUMER_SECRET=config.get('main','CONSUMER_SECRET')
    ACCESS_KEY=config.get('main','ACCESS_KEY')
    ACCESS_SECRET=config.get('main','ACCESS_SECRET')
    auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
    api=tweepy.API(auth)
    timeline=api.public_timeline()
    return timeline

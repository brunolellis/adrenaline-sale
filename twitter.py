import tweepy
from credentials import *

class Twitter(object):
    auth = None
    api = None

    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(self.auth)

    def publish(self, message):
        try:
            self.api.update_status(message)
        except tweepy.error.TweepError:
            pass
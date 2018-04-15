import tweepy
import os

# https://apps.twitter.com

class Twitter(object):
    auth = None
    api = None

    def __init__(self):
        consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
        consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        access_token = os.environ["TWITTER_ACCESS_TOKEN"]
        access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
        self.auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(self.auth)

    def publish(self, message):
        try:
            self.api.update_status(message)
        except tweepy.error.TweepError:
            pass
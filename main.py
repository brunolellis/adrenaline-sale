import datetime as dt
from adrenaline_feed import *
from publication_handler import *
from twitter import *

def main():
    p = PublicationHandler()
    since = p.get_last_published_date()

    feed = AdrenalineFeed()
    feed.parse()

    new_items = feed.get_new_items_since(since)
    new_items.reverse()

    twitter = Twitter()
    for i in new_items:
        tweet = i.title + ' ' + i.link
        #print(tweet)
        twitter.publish(tweet)

    p.set_last_published_date(feed.get_most_recent_published_date())

    print("concluido com sucesso")
import datetime as dt
from adrenaline_feed import *
from twitter import *

def main():
    
    feed = AdrenalineFeed()
    feed.parse()
    items = feed.get_unpublished_items()
    items.reverse()
    
    published_items = 0
    twitter = Twitter()
    for i in items:
        tweet = i.title + ' ' + i.link
        #print(tweet)
        twitter.publish(tweet)
        feed.publish(i)
        published_items = published_items + 1

    print("concluido com sucesso: ", published_items)

if __name__ == '__main__':
    main()
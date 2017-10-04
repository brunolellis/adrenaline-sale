import feedparser
import time
from time import mktime
from datetime import datetime
from datetime import timezone
from publication_handler import *

class AdrenalineFeed(object):
    url = None
    contents = None
    publisher = None

    def __init__(self):
        self.url = 'https://adrenaline.uol.com.br/forum/forums/for-sale.221/index.rss'
        self.publisher = PublicationHandler()

    def parse(self):
        self.contents = feedparser.parse(self.url)

    def get_unpublished_items(self):
        items = []
        for i in self.contents['entries']:
            if not self.publisher.is_link_published(i.link):
                items.append(i)
        
        return items

    def publish(self, post):
        self.publisher.publish(post)

    def debug(self):
        print(self.contents['entries'][0]['id'])
        print(self.contents['entries'][0]['link'])
        print(self.contents['entries'][0]['title'])
        print(self.contents['entries'][1]['id'])
        print(self.contents['entries'][1]['link'])
        print(self.contents['entries'][1]['title'])
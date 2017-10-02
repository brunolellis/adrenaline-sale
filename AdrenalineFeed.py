import feedparser
import time
from time import mktime
from datetime import datetime
from datetime import timezone

class AdrenalineFeed(object):
    url = None
    contents = None

    def __init__(self):
        self.url = 'https://adrenaline.uol.com.br/forum/forums/for-sale.221/index.rss'

    def parse(self):
        self.contents = feedparser.parse(self.url)

    def get_most_recent_published_item(self):
        e = self.contents['entries'][0]
        return datetime.fromtimestamp(mktime(e['published_parsed']))

    def get_new_items_since(self, since):
        new_entries = []
        for e in self.contents['entries']:
            dt = datetime.fromtimestamp(mktime(e['published_parsed']))
            if dt > since:
                new_entries.append(e)
        return new_entries

    def debug(self):
        print(self.contents['entries'][0]['id'])
        print(self.contents['entries'][0]['link'])
        print(self.contents['entries'][0]['title'])
        print(self.contents['entries'][1]['id'])
        print(self.contents['entries'][1]['link'])
        print(self.contents['entries'][1]['title'])
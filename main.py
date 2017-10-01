import feedparser
from credentials import *


d = feedparser.parse('https://adrenaline.uol.com.br/forum/forums/for-sale.221/index.rss')

print(d['entries'][0]['id'])
print(d['entries'][0]['link'])
print(d['entries'][0]['title'])
print(d['entries'][1]['id'])
print(d['entries'][1]['link'])
print(d['entries'][1]['title'])
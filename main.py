import datetime as dt
from credentials import *
from AdrenalineFeed import *

a = AdrenalineFeed()
a.parse()

yesterday = dt.datetime(2017, 10, 30)

print(a.get_new_items_since(yesterday))

print(a.get_most_recent_published_item())
#a.debug()
#REDIS_URL: redis://h:p0a8fdfdc4798fe483113b712fa51c85960f30239b22c1597fe2a115a68f32062@ec2-34-206-56-226.compute-1.amazonaws.com:59799

import os
import psycopg2
from urllib import parse
import datetime

class PublicationHandler(object):

    def __init__(self):
        parse.uses_netloc.append("postgres")
        url = parse.urlparse(os.environ["DATABASE_URL"])
        try:
            self.conn = psycopg2.connect(
                database=url.path[1:],
                user=url.username,
                password=url.password,
                host=url.hostname,
                port=url.port
            )
        except e:
            print("Unable to connect to the database", e)
    
    def get_last_published_date(self):
        cur = self.conn.cursor()
        cur.execute("SELECT last_date FROM last_publication")
        rows = cur.fetchall()
        if len(rows) == 0:
            return datetime.datetime.now()
        else:
            return rows[0][0]

    def set_last_published_date(self, date):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM last_publication")
        cur.execute("INSERT INTO last_publication VALUES (%s)", (date, ))
        self.conn.commit()

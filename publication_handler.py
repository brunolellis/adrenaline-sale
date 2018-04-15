import os
import psycopg2
from urllib import parse
import datetime

class PublicationHandler(object):

    def connect(self):
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
    
    def close(self):
        self.conn.commit()
        self.conn.close()

    def is_link_published(self, link):
        self.connect()
        cur = self.conn.cursor()

        thread_id = self.get_thread_id(link)
        cur.execute("SELECT count(1) FROM posts WHERE thread_id = %s", (thread_id, ))
        c = cur.fetchone()

        cur.close()
        self.close()        
        return c[0] == 1

    def publish(self, post):
        self.connect()
        cur = self.conn.cursor()

        thread_id = self.get_thread_id(post.link)
        cur.execute("INSERT INTO posts (thread_id) VALUES (%s)", (thread_id, ))
        
        cur.close()
        self.close()

    def get_thread_id(self, link):
        # https://adrenaline.uol.com.br/forum/threads/steam-tomb-raider-goty-r-12-75.621328/
        return int(link.split('.')[-1].replace('/',''))
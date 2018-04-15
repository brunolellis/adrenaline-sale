# Adrenaline sale
Parser das últimas promoções criadas no fórum [Adrenaline FOR SALE!](https://adrenaline.uol.com.br/forum/forums/for-sale.221/) e divulgadas no Twitter [@adrenaline_sale](https://twitter.com/adrenaline_sale).

Utiliza python (APScheduler e feedparser), postgresql (psycopg2), heroku e twitter (tweepy).

## Configurações
### heroku
- PostgreSQL:
    `heroku config:set DATABASE_URL=postgres://qwerty:zxcvbn@compute-1.amazonaws.com:5432/db`
- Twitter:
    `heroku config:set TWITTER_CONSUMER_KEY=a`
    `heroku config:set TWITTER_CONSUMER_SECRET=b`
    `heroku config:set TWITTER_ACCESS_TOKEN=c`
    `heroku config:set TWITTER_ACCESS_TOKEN_SECRET=d`


### PostgreSQL
`CREATE TABLE posts (id serial PRIMARY KEY, thread_id integer NOT NULL);`
`CREATE INDEX idx_posts_tid ON posts (thread_id);`

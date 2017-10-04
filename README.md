### Postgres local
`export DATABASE_URL=postgres:///$(whoami)`


CREATE TABLE last_publication (last_date timestamp NOT NULL);
INSERT INTO last_publication VALUES (date '2017-09-20');


DROP TABLE last_publication;

CREATE TABLE posts (id serial PRIMARY KEY, thread_id integer NOT NULL);
CREATE INDEX idx_posts_tid ON posts (thread_id);

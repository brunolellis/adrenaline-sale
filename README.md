### Postgres local
`export DATABASE_URL=postgres:///$(whoami)`


CREATE TABLE last_publication (last_date timestamp NOT NULL);
INSERT INTO last_publication VALUES (date '2017-09-20');
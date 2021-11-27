CREATE SEQUENCE user_id_seq
    start with 7;

CREATE TYPE Role_names AS ENUM ( 'ROLE_ADMIN', 'ROLE_USER');

CREATE TABLE public.User_1 (
                               User_ID BIGINT NOT NULL default nextval('user_id_seq'),
                               Role_name VARCHAR NOT NULL,
                               FIO VARCHAR NOT NULL,
                               Email VARCHAR,
                               Password VARCHAR,
                               CONSTRAINT user_id PRIMARY KEY (User_ID)
);

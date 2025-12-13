-- create users
-- depends: 

CREATE TABLE users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    password_hash BYTEA NOT NULL,
    email VARCHAR(64) NOT NULL,
    email_confirmed BOOLEAN DEFAULT false,
    CONSTRAINT unique_email_confirmed UNIQUE (email, email_confirmed)
);
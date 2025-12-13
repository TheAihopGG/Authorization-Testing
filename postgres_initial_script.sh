#!/bin/bash
set -e
# выглядит как костыль, потом заменить
psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
    CREATE DATABASE authorization_database;
    CREATE USER authorization_api WITH PASSWORD '$AUTHORIZATION_API_USER_PASSWORD';
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO authorization_api;
EOSQL
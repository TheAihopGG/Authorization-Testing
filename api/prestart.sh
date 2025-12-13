#!/bin/bash
set -e
yoyo apply -b --database postgresql+psycopg://authorization_api:$POSTGRES_PASSWORD@postgres:5432/authorization_database
echo Migrations applied
exec "$@"
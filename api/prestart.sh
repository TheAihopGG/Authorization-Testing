#!/bin/sh
set -e
echo Applying migrations
yoyo apply --database mysql://$POSTGRES_USERNAME:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB --batch
echo Migrations applied
exec "$@"
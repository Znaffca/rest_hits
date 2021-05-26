#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.5
    done
    echo "Postgresql started!"
fi

python manage.py create_db

python manage.py create_data

exec "$@"
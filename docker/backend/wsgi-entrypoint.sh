#!/bin/sh

until cd /app/
do
    echo "Waiting for volume ready..."
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py collectstatic --noinput
if [ "$1" = "" ]; then
  gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 1 --threads 4
else
  exec "$@"
fi

#####################################################################################
# Options to DEBUG Django server
# Optional commands to replace above gunicorn command

# Option 1:
# run gunicorn with debug log level
# gunicorn server.wsgi --bind 0.0.0.0:8000 --workers 1 --threads 1 --log-level debug

# Option 2:
# run development server
# DEBUG=True ./manage.py runserver 0.0.0.0:8000
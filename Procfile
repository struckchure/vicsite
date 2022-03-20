release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn site_server.wsgi --log-file -
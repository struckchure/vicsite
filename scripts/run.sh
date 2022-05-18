docker-compose run --rm api python manage.py migrate
docker-compose up -d --force-recreate --build

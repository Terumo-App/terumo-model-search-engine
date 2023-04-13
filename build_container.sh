pipenv requirements > requirements.txt
docker build -t terumo-service-search-engine .

docker tag terumo-service-search-engine terumoapp/terumo-service-search-engine:latest

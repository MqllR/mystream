## INSTALLATION

* DOCKER

To run this application in docker:

1- Run a RabbitMQ docker:
```
docker pull rabbitmq:3
docker run -d --hostname rabbit --name rabbit rabbitmq:3
```

2- Run the mystream-app docker:
```
docker pull registry.gitlab.com:Mqll/mystream:app
docker run -d -v <path/to/media>:/opt/media -v /var/log/gunicorn:/var/log/gunicorn  -v <path/to/static>:/static -v <path/to/db>:/opt/db.sqlite3 -p 8000:8000 --name mystream-app --link rabbit:rabbit registry.gitlab.com:Mqll/mystream:app
```

3- Run the mystream-encode docker:
```
docker pull registry.gitlab.com:Mqll/mystream:encode
docker run -d -v '<path/to/media>':'/opt/media' -v '/var/log/celery':'/var/log/celery' -v <path/to/db>:/opt/db.sqlite3 --name mystream-encode --link rabbit:rabbit registry.gitlab.com:Mqll/mystream:encode
```

4- Run the nginx docker:
```
docker run -d -p 80:80 --name nginx --link mystream-app:mystream-app -v <path/to/nginx.conf>:/etc/nginx/nginx.conf -v <path/to/media>:/opt/mystream/media -v <path/to/static>:/opt/mystream/static nginx
```

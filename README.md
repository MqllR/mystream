## INSTALLATION

* Application:
```
pip install -r requirements.txt
mkdir -p media/{stream,tmp}
python manage.py migrate
python manage.py createsuperuser
```
* Supervisor:
```
cp conf/supervisor/* /etc/supervisor/conf.d/
```
* Nginx:
```
cp conf/nginx/* /etc/nginx/sites-available/
```
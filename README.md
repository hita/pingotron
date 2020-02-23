# pingS

pingS is a webApp. It consists of a HTTP-ping-based health monitor to keep track of site availabity and speed. A cron job will check every few seconds the status and delay for each service. A negative delay (-9000 ms) means "service down". The GUID will show real-time charts of the monitored services. 

### Installing

1. Run docker compose up

```
sudo docker-compose up
```

2. Migrate database

```
python manage.py migrate
```

3. Create init admin user and provide login data

```
python manage.py createsuperuser
```
### Usage

1. Enter http://0.0.0.0:8000 on a browser
2. Go to "Admin" (django Admin) or http://0.0.0.0:8000/admin/
3. Enter admin login
4. Scroll to Targets and click on "add" to create a new service to monitor: 
4.1 Path = URL of the HTTP service 
4.2 Alias = short name of the service
4.3 Description = (optional) description of the service
5. Click on "save"
6. Go back to http://0.0.0.0:8000


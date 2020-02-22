import socket
from .models import *
from urllib.request import urlopen
from django.utils.timezone import now
import time
import datetime

def pingServer(url):
    socket.setdefaulttimeout( 20 )  # timeout in seconds
    
    try :
        response = urlopen( url )
    except :
        return False
    else :
        html = response.read()
        return True

def updateTargets():

    all_servers = Target.objects.all()
    is_online = False

    for server in all_servers:
        delay = -9000
        new_datetime = now()
        server.date_last_ping = new_datetime
        is_online = pingServer(server.path)
        if is_online:
            server.status_choices = "ON"
            server.date_last_online = new_datetime
            delay = (now()-new_datetime).seconds*1000
        else:
            server.status_choices = "OFF"
        server.save()
        
        print(f'{server.alias} : {delay} ms')
        record = Register(date_creation = server.date_last_ping, is_active = is_online, delay_ms = delay, target=server)
        
        record.save()

        
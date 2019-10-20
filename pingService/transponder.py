import socket
from .models import Target 
from urllib.request import urlopen
from django.utils.timezone import now

def pingServer(url):
    socket.setdefaulttimeout( 23 )  # timeout in seconds
    
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
        server.date_last_ping = now()
        is_online = pingServer(server.path)
        if is_online:
            server.status_choices = "ON"
            server.date_last_online = now()
        else:
            server.status_choices = "OFF"
        
        server.save()

        
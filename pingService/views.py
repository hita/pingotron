from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from .transponder import *

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

def status(ip_address):
    return True

def index(request):

    updateTargets()
    
    all_servers = Target.objects.all()
    context = {'all_servers': all_servers}
    return render(request, 'home.html', context)

def charts(request):

    updateTargets()
    
    all_servers = Target.objects.all()
    context = {'all_servers': all_servers}
    return render(request, 'charts.html', context)

def get_data(request, *args, **kwargs):
    
    labels = []
    delay = []
    production_server = Target.objects.filter(alias="Blog")
    earlier = now()-datetime.timedelta(minutes=30)
    production_records = Register.objects.filter(target=production_server[0])
  
    for record in production_records:
        labels.append(record.date_creation)
        delay.append(record.delay_ms)
   

    data = {
        "labels": labels,
        "delay": delay,
    }
    return JsonResponse(data) # http response

class ServerData(APIView):
    authentication_classes = []
    premission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue"]
        default_items = [qs_count, 23]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
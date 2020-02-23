from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.core import serializers
import json


from .transponder import *
from .sampler import *

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import *

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


def status(ip_address):
    return True


def index(request):

    all_servers = Target.objects.all()
    context = {'all_servers': all_servers}
    timeLabels = getTimeLabels(5, 30)
    return render(request, 'home.html', context)


def charts(request):

    updateTargets()
    all_servers = Target.objects.all()
    context = {'all_servers': all_servers}
    return render(request, 'charts.html', context)


def get_data(request, *args, **kwargs):
    
    data = produceDelayObject()
    return JsonResponse(data, safe=False)  # http response

def get_status(request):
    server_id = request.GET.get('server_id')
    status = "unknown"
    if server_id is not None:
        try:
            server = Target.objects.get(id=server_id)
            status = server.status_choices
            data = {
                "server-id": server_id,
                "status": status,
            }
            return JsonResponse(data)
        except:
            data = {
                "server-id": server_id,
                "status": "unknown",
            }
            return JsonResponse(data)

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

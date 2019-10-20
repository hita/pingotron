from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from .transponder import *


def status(ip_address):
    return True

def index(request):

    updateTargets()
    
    all_servers = Target.objects.all()
    context = {'all_servers': all_servers}
    return render(request, 'home.html', context)
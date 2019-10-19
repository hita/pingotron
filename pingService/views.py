from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1>Pingotron is online</h1>")

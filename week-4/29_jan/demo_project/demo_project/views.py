from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, this is views.py file of demo_project app')


def addition(request):
    return HttpResponse(5+6)

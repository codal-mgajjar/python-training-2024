from django.http import HttpResponse

def addition(request):
    return HttpResponse(5+6)

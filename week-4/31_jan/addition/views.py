from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def addition(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))

        result = num1 + num2
        return HttpResponse(f"{result}")
    return render(request, 'addition/addition.html')
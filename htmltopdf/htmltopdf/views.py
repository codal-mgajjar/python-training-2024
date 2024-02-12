# chartapp/views.py

from django.shortcuts import render

def chart_to_pdf(request):
    return render(request, '/templates/index.html')

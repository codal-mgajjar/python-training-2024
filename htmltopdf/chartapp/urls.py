# chartapp/urls.py

from django.urls import path
from .views import google_chart_to_pdf, generate_pdf

urlpatterns = [
    path('google-chart-to-pdf/', google_chart_to_pdf, name='google_chart_to_pdf'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),
]

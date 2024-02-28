from django.urls import path
from .views import chart_view, generate_pdf

urlpatterns = [
    path("chart/", chart_view, name="chart-view"),
    path("pdf/", generate_pdf.as_view(), name="pdf"),
]

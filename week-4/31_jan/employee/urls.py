from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('show_employee/', views.show_employee, name='show_employee'),
    path('add/', views.add_employee, name='add_employee'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

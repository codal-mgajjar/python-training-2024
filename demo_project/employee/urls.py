from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.show_employee, name="show_employee"),
    path("add_employee/", views.add_employee, name="add_employee"),
    path(
        "delete_employee/<int:employee_id>/",
        views.delete_employee,
        name="delete_employee",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

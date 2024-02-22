from django.urls import path
from .views import ItemListView, hello_world, view, view_schema_decorator, UserList

urlpatterns = [
        path('items/',ItemListView.as_view(),name="item-list"),
        path('hello/', hello_world, name="hello-world"),
        path('view/', view, name="view"),
        path('view_schema_decorator/', view_schema_decorator, name="view_schema_decorator"),
        path('users/', UserList.as_view(), name='user-list')

]
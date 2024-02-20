from django.urls import path
from .views import ItemListView, hello_world, view, view_schema_decorator, UserList, UserViewSet, ExampleView, UserCountView

user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
        path('items/',ItemListView.as_view(),name="item-list"),
        path('hello/', hello_world, name="hello-world"),
        path('example_view/', ExampleView.as_view(), name="example-view"),
        path('view/', view, name="view"),
        path('view_schema_decorator/', view_schema_decorator, name="view_schema_decorator"),
        # path('users/', UserList.as_view(), name='user-list')
        path('user_count/', UserCountView.as_view(), name="UserCountView"),

]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


# Router example 
from .views import ItemsViewSet
router.register('item', ItemsViewSet, basename='item')
urlpatterns += router.urls

# Using include
# urlpatterns = [
#     path('', include(router.urls)),
# ]


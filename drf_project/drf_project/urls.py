"""
URL configuration for drf_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from quickstart.views import UserViewSet, GroupViewSet 
from rest_framework import renderers
from snippets.views import api_root, SnippetViewSet, UserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

snippet_list = SnippetViewSet.as_view({'get': 'list','post': 'create'})
snippet_detail = SnippetViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update','delete': 'destroy'})
snippet_highlight = SnippetViewSet.as_view({'get': 'highlight'}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')
urlpatterns = [path('', include(router.urls)),]
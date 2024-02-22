from django.urls import path, include
from .views import RegisterUser, LoginView, LogoutView
urlpatterns = [
    path('register/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(),name="logout")
]

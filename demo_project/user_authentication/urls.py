from django.urls import path, include
from .views import authView,home, login_view

app_name = "user_authentication"

urlpatterns = [
    
    path("accounts/", include("django.contrib.auth.urls")),
    
    path("accounts/login/",login_view,name="login"),
    path("signup/", authView, name= "authView"),
    path("",home,name="home"),

]
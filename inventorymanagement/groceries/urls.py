from django.urls import path, include
from .views import RegisterUser, LoginView, LogoutView, ProductListView, CategoryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("products", ProductListView, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", include(router.urls)),
]

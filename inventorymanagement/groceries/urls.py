from django.urls import path, include
from .views import (
    RegisterUser,
    LoginView,
    LogoutView,
    success_view,
    ProductListView,
    PurchaseViewSet,
    CategoryViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("products", ProductListView, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"purchase_product", PurchaseViewSet, basename="purchase_product")

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("success/", success_view, name="success_view"),
    path(
        "<int:pk>/create-stripe-checkout-session/",
        ProductListView.as_view({"post": "create_stripe_checkout_session"}),
        name="create_stripe_checkout_session",
    ),
    path("", include(router.urls)),
]

from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    LoginUserSerializer,
    ProductSerializer,
    CategorySerializer,
    PurchaseSerializer,
)
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import viewsets, mixins, generics, status, filters
from rest_framework.decorators import action
from .permissions import ReadOnly
from .models import Product, Category, Purchase, PaymentConfirmation
import stripe
from django.conf import settings
from django.shortcuts import HttpResponse


class RegisterUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "status": status.HTTP_403_FORBIDDEN,
                    "errors": serializer.errors,
                    "message": "Something went wrong",
                }
            )

        user = serializer.save()

        return Response(
            {
                "status": status.HTTP_200_OK,
                "payload": serializer.data,
                "message": "you data is registered",
            }
        )


class LoginView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginUserSerializer(
            data=request.data, context={"request": request}
        )
        if not serializer.is_valid():
            return Response(
                {
                    "status": status.HTTP_403_FORBIDDEN,
                    "errors": serializer.errors,
                    "message": "Something went wrong",
                }
            )

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Invalid credentials",
                }
            )

        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data
        data["token"] = str(token)
        return Response(
            {
                "data": data,
                "status": status.HTTP_200_OK,
                "message": "Login successful",
            }
        )


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        request.auth.delete()
        return Response({"status": status.HTTP_200_OK, "message": "Logout successful"})


class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description", "price", "quantity"]
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & ReadOnly | IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=["PATCH"])
    def update_product(self, request, pk=None):
        try:
            instance = self.get_object()

            serializer = ProductSerializer(instance, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Item updated successfully."})
            else:
                return Response(
                    {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
                )

        except Product.DoesNotExist:
            return Response(
                {"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=["DELETE"])
    def delete_product(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.delete()

            return Response(
                {"detail": "Item deleted successfully."}, status=status.HTTP_200_OK
            )

        except Product.DoesNotExist:
            return Response(
                {"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @action(
        detail=True,
        methods=["POST"],
    )
    def purchase_product(self, request, pk=None):
        try:
            product = self.get_object()
            quantity_to_purchase = request.data.get("quantity", 1)

            if product.quantity < quantity_to_purchase:
                return Response(
                    {"error": "Insufficient quantity available."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            purchase_data = {
                "customer": request.user.id,
                "product": product.id,
                "quantity": quantity_to_purchase,
            }

            purchase_serializer = PurchaseSerializer(data=purchase_data)

            if purchase_serializer.is_valid():
                purchase_serializer.save()
                product.quantity -= quantity_to_purchase
                product.save()
                return Response({"detail": "Purchase successful."})
            else:
                return Response(
                    {"error": purchase_serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=["GET"])
    def get_user_purchases(self, request):
        user = request.user
        purchases = Purchase.objects.filter(customer=user)

        if not purchases.exists():
            return Response(
                {"detail": "No purchases found for the user."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated & ReadOnly | IsAdminUser]


class PurchaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    stripe.api_key = settings.STRIPE_SECRET_KEY

    @action(detail=True, methods=["POST"])
    def create_stripe_checkout_session(self, request, pk=None):
        prod_id = pk
        quantity = request.data.get("quantity", 1)

        try:
            product = Product.objects.get(id=prod_id)

            if int(product.quantity) < int(quantity):
                return Response(
                    {"error": "Insufficient quantity available."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            overall_price = int(product.price) * quantity

            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "unit_amount": overall_price * 100,
                            "product_data": {
                                "name": product.name,
                            },
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                metadata={
                    "product_id": product.id,
                    "quantity": quantity,
                },
                success_url="http://localhost:8000/groceries/success/?session_id={{CHECKOUT_SESSION_ID}}",
                cancel_url=settings.SITE_URL + "?cancel=true",
            )
            session_id = checkout_session.id

            return Response(
                {"checkout_url": checkout_session.url, "session_id": session_id},
                status=status.HTTP_200_OK,
            )

        except Product.DoesNotExist:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    @action(detail=False, methods=["POST"])
    def confirm_payment(self, request, *args, **kwargs):
        try:
            session_id = request.data.get("session_id")

            if PaymentConfirmation.objects.filter(session_id=session_id).exists():
                return Response(
                    {"error": "Payment already confirmed for this session ID."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            checkout_session = stripe.checkout.Session.retrieve(session_id)

            product_id = checkout_session.metadata.get("product_id")
            quantity = checkout_session.metadata.get("quantity")

            product = Product.objects.get(id=product_id)

            if int(product.quantity) < int(quantity):
                return Response(
                    {"error": "Insufficient quantity available."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            purchase_data = {
                "customer": request.user.id,
                "product": product.id,
                "quantity": quantity,
            }

            purchase_serializer = PurchaseSerializer(data=purchase_data)

            if purchase_serializer.is_valid():
                remaining_quantity = int(product.quantity) - int(quantity)
                product.quantity = max(remaining_quantity, 0)
                product.save()

                purchase_serializer.save()

                PaymentConfirmation.objects.create(
                    product=product, customer=request.user, session_id=session_id
                )

                return Response({"detail": "Purchase successful."})
            else:
                return Response(
                    {"error": purchase_serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            print(e)
            return Response(
                {"detail": "Unsuccessful payment confirmation."},
                status=status.HTTP_400_BAD_REQUEST,
            )


def success_view(request):
    session_id = request.GET.get("session_id")
    return HttpResponse(f"Success! Session ID: {session_id}")

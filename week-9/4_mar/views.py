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
from .models import Product, Category, Purchase


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

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Category, Purchase, PaymentConfirmation
from django.core.validators import RegexValidator
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def validate_category_ids(self, value):
        if not Category.objects.filter(id__in=value).exists():
            raise serializers.ValidationError(
                "One or more selected categories do not exist."
            )
        return value

    def create(self, validated_data):
        category_ids = validated_data.pop("categories", [])
        validated_data["created_by"] = self.context["request"].user
        product = super().create(validated_data)
        product.categories.set(category_ids)
        return product

    def validate_category_ids(self, value):
        if not Category.objects.filter(id__in=value).exists():
            raise serializers.ValidationError(
                "One or more selected categories do not exist."
            )
        return value

    def create(self, validated_data):
        category_ids = validated_data.pop("categories", [])
        validated_data["created_by"] = self.context["request"].user
        product = super().create(validated_data)
        product.categories.set(category_ids)
        return product


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z\s]+$",
                message="Name can only contain letters and spaces.",
                code="invalid_name",
            ),
        ],
    )

    class Meta:
        model = Category
        fields = ["id", "name"]


class PurchaseSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Purchase
        fields = [
            "id",
            "customer",
            "product",
            "quantity",
            "purchase_date",
            "product_name",
        ]

    def get_product_name(self, obj):
        return obj.product.name


import datetime

from rest_framework import serializers


def check_expiry_month(value):
    if not 1 <= int(value) <= 12:
        raise serializers.ValidationError("Invalid expiry month.")


def check_expiry_year(value):
    today = datetime.datetime.now()
    if not int(value) >= today.year:
        raise serializers.ValidationError("Invalid expiry year.")


def check_cvc(value):
    if not 3 <= len(value) <= 4:
        raise serializers.ValidationError("Invalid cvc number.")


def check_payment_method(value):
    payment_method = value.lower()
    if payment_method not in ["card"]:
        raise serializers.ValidationError("Invalid payment_method.")


class CardInformationSerializer(serializers.Serializer):
    card_number = serializers.CharField(max_length=150, required=True)
    expiry_month = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_expiry_month],
    )
    expiry_year = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_expiry_year],
    )
    cvc = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_cvc],
    )


class PaymentConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentConfirmation
        fields = "__all__"

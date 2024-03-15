from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Category, Purchase, PaymentConfirmation
from django.core.validators import RegexValidator
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format")

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")

        return value


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise serializers.ValidationError(
                "Both username and password are required."
            )

        return data


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


class PaymentConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentConfirmation
        fields = "__all__"


class ActivationSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    token = serializers.CharField()

    def validate(self, data):
        user = data["user"]
        token = data["token"]
        token_generator = PasswordResetTokenGenerator()

        if not token_generator.check_token(user, token):
            raise serializers.ValidationError("User already activated")

        return data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

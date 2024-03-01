from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Category
from django.core.validators import RegexValidator


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

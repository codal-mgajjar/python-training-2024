from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.name


class Purchase(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.customer.username} purchased {self.quantity} of {self.product.name}"
        )


class RequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.ip_address:
            self.ip_address = "127.0.0.1"  # Default IP address
        super(RequestLog, self).save(*args, **kwargs)


class PaymentConfirmation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmed_at = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=255, unique=True, default=None)

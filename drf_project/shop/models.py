from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class temp(models.Model):
    t1 = models.CharField(max_length=100, default=None)


class Item(models.Model):
    name = models.CharField(max_length=100, default=None)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=None,
        validators=[
            MinValueValidator(limit_value=0),
        ],
    )
    category = models.CharField(max_length=50, default=None)
    t1 = models.ForeignKey(temp, on_delete=models.CASCADE, default=None)
    t2 = models.ManyToManyField(temp, related_name="items_t2")

    def __str__(self):
        return self.name


class TestFields(models.Model):
    test_field = models.CharField(max_length=50, default=None)

    class Meta:
        abstract = True


class Abstracted_class(TestFields):
    test_field2 = models.CharField(max_length=50, default=None)

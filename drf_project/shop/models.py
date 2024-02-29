from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


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

    def __str__(self):
        return self.name

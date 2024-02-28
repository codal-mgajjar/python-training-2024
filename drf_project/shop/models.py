from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

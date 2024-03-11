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


class Book(models.Model):
    title = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, through="BookAuthor")


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_added = models.DateField()


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, through="ProductCategory")


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateField()


class Player(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=16)
    players = models.ManyToManyField(Player, through="Roster")

    def __str__(self):
        return self.name


class Roster(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=16, null=True)
    game_day = models.DateTimeField(auto_now_add=True)

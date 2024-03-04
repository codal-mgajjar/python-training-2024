from django.core.management.base import BaseCommand
from groceries.models import Product


class Command(BaseCommand):
    help = "List all Products"

    def handle(self, *args, **optional):
        products = Product.objects.all()

        self.stdout.write(self.style.SUCCESS("List of products: "))
        for product in products:
            self.stdout.write(
                self.style.SUCCESS(f" - {product.name} (Price: ${product.price})")
            )

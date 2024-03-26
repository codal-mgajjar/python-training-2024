from django.core.management.base import BaseCommand
from groceries.models import Product


class Command(BaseCommand):
    help = "Update the quantity of specific product"

    def add_arguments(self, parser):
        parser.add_argument("product_id", type=int, help="ID of the product")
        parser.add_argument("new_quantity", type=int, help="Quantity of the product")

    def handle(self, *args, **options):
        product_id = options["product_id"]
        new_quantity = options["new_quantity"]

        try:
            product = Product.objects.get(pk=product_id)
            product.quantity = new_quantity
            product.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Quantity of product '{product.name}' updated to {new_quantity}"
                )
            )
        except Product.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(f"Product with ID {product_id} does not exist")
            )

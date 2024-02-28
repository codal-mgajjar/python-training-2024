from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Product


@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs):
    if created:
        print(f"Product {instance.name} created by {instance.created_by}")
    else:
        print(f"Product {instance.name} updated by {instance.created_by}")


@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, **kwargs):
    print(f"Product {instance.name} deleted by {instance.created_by}")


@receiver(m2m_changed, sender=Product.categories.through)
def product_categories_changed(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        print(f"Categories added to product {instance.name}: {pk_set}")
    elif action == "post_remove":
        print(f"Categories removed from product {instance.name}: {pk_set}")
    elif action == "post_clear":
        print(f"All categories removed from product {instance.name}")

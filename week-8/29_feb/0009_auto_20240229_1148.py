from django.db import migrations, models


def add_new_field(apps, schema_editor):
    Item = apps.get_model("shop", "Item")
    new_field = models.CharField(max_length=50, default="Custom Default Value")
    new_field.contribute_to_class(Item, "new_field")


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_merge_0006_auto_20240229_1133_0007_item_test_field"),
    ]

    operations = [
        migrations.RunPython(add_new_field),
    ]

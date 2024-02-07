# Generated by Django 4.2.9 on 2024-02-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_product_has_edeka_article_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="edeka_article_number",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="gross_weight",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="net_weight",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="validation_status",
            field=models.CharField(
                blank=True,
                choices=[("Validated", "Validated"), ("Unvalidated", "Unvalidated")],
                max_length=255,
                null=True,
            ),
        ),
    ]

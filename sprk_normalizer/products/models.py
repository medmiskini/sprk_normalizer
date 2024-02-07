from django.db import models
from sprk_normalizer.products.enums import *

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=255)
    trade_item_unit_descriptor = models.CharField(max_length=255, null=True, blank=True)
    trade_item_unit_descriptor_name = models.CharField(max_length=255, null=True, blank=True)
    amount = models.PositiveIntegerField(default=0, blank=False, null=False)
    brand = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    has_edeka_article_number = models.BooleanField(default=False)
    edeka_article_number =models.CharField(max_length=255, null=True, blank=True)
    gross_weight = models.FloatField(null=True, blank=True)
    net_weight = models.FloatField(null=True, blank=True)
    packaging = models.CharField(max_length=255, null=True, blank=True)
    validation_status = models.CharField(max_length=255, choices=ValidationStatus.CHOICES, null=True, blank=True)
    unit_name  = models.CharField(max_length=255, null=True, blank=True)
    

    def __str__(self):
        return f'Product {self.code}_{self.type}'

    class Meta:
        ordering = ['code']
        unique_together = (('code', 'type'),)
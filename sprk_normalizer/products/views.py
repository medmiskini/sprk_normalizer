from sprk_normalizer.products.models import Product
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from products.serializers import ProductSerializer

# Create your views here.

class ProductsDetail(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [] #disables authentication
    permission_classes = []
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductsList(mixins.CreateModelMixin, mixins.ListModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [] #disables authentication
    permission_classes = []

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED, headers=headers)
    
    @transaction.atomic
    def perform_create(self, serializer):
        products = serializer.validated_data.get('products')
        existing_records = {}

        # create or update the products
        for entry in products:
            code = entry.get('code')
            product_type = entry.get('type')
            existing_product = Product.objects.filter(code=code, type=product_type).first()
            if existing_product:
                existing_product.amount += entry.get('amount')
                for field in entry:
                    if field != 'amount':
                        setattr(existing_product, field, entry.get(field))
                existing_records[(code, product_type)] = existing_product
            else:
                Product.objects.create(**entry)

        # Bulk update existing records
        Product.objects.bulk_update(
            list(existing_records.values()), 
            ['trade_item_unit_descriptor', 'trade_item_unit_descriptor_name', 'amount', 'brand', 
             'description', 'has_edeka_article_number', 'edeka_article_number', 'gross_weight', 
             'net_weight', 'packaging', 'validation_status', 'unit_name']
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
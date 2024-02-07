from django.urls import path
from sprk_normalizer.products.views import ProductsDetail, ProductsList

urlpatterns = [
    path('products/<str:pk>/', ProductsDetail.as_view()),
    path('products/', ProductsList.as_view())
]
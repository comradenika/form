from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path("product/", product_list, name='product_list'),
    path("product_details/<int:pk>", product_detail, name='product_detail'),
]

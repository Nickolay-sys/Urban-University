from django.urls import path
from .views import product_list, add_product

urlpatterns = [
    # Главная страница
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
]
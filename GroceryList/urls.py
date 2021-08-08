from django.urls import path

from .views import (
    home,
    products,
    products_under_category
)

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('products/category/', products_under_category, name='products_under_category_all'),
    path('products/category/<int:category_id>', products_under_category, name='products_under_category'),
    path('list-category/all/', home, name='list_category_all'),
    path('list-category/<int:pk>', home, name='list_category')
]
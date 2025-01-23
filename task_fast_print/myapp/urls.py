from django.urls import path
from .views import product_list, product_create, product_update, product_delete

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/add/', product_create, name='product_create'),
    path('product/edit/<int:pk>/', product_update, name='product_update'),
    path('product/delete/<int:pk>/', product_delete, name='product_delete'),
]
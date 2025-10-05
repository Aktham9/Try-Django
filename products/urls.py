from django.urls import path
from .views import *
app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('create/', product_create_view, name='product-list'),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),

]
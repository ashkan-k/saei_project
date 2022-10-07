from django.urls import path
from .views import *

urlpatterns = []
 
dashboard_urls = [
    path('dashboard/categories/', CategoriesListView.as_view(), name='categories-list'),
    path('dashboard/categories/create/', CategoriesCreateView.as_view(), name='categories-create'),
    path('dashboard/categories/update/<int:pk>/', CategoriesUpdateView.as_view(), name='categories-update'),
    path('dashboard/categories/delete/<int:pk>/', CategoriesDeleteView.as_view(), name='categories-delete'),

    path('dashboard/products/', ProductsListView.as_view(), name='products-list'),
    path('dashboard/products/create/', ProductsCreateView.as_view(), name='products-create'),
    path('dashboard/products/update/<int:pk>/', ProductsUpdateView.as_view(), name='products-update'),
    path('dashboard/products/delete/<int:pk>/', ProductsDeleteView.as_view(), name='products-delete'),

    path('dashboard/user/products/', UserProductsListView.as_view(), name='user-products-list'),
    path('dashboard/user/products/delete/<int:pk>/', UserProductsDeleteView.as_view(), name='user-products-delete'),
]

front_urls = [
    path('products/', Products.as_view(), name='products-user-list'),
    path('products/<str:slug>/', ProductsDetail.as_view(), name='products-user-detail'),
    path('products/categories/<str:slug>/', Products.as_view(), name='category-products'),
]

urlpatterns += dashboard_urls
urlpatterns += front_urls

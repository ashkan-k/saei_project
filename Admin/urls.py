from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    path('dashboard/images/', DashboardImagesList.as_view(), name='images-list'),
    path('dashboard/images/create/', DashboardImagesCreate.as_view(), name='images-create'),
    path('dashboard/images/update/<int:pk>/', DashboardImagesUpdate.as_view(), name='images-update'),
    path('dashboard/images/delete/<int:pk>/', DashboardImagesDelete.as_view(), name='images-delete'),
]

from django.urls import path
from .views import *

urlpatterns = []
 
dashboard_urls = [
    path('dashboard/helps/', HelpsListView.as_view(), name='helps-list'),
    path('dashboard/helps/create/', HelpsCreateView.as_view(), name='helps-create'),
    path('dashboard/helps/update/<int:pk>/', HelpsUpdateView.as_view(), name='helps-update'),
    path('dashboard/helps/delete/<int:pk>/', HelpsDeleteView.as_view(), name='helps-delete'),
]

urlpatterns += dashboard_urls

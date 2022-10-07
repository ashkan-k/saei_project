from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/sliders/', SlidersListView.as_view(), name='sliders-list'),
    path('dashboard/sliders/create/', SlidersCreateView.as_view(), name='sliders-create'),
    path('dashboard/sliders/update/<int:pk>/', SlidersUpdateView.as_view(), name='sliders-update'),
    path('dashboard/sliders/delete/<int:pk>/', SlidersDeleteView.as_view(), name='sliders-delete'),
]

urlpatterns += dashboard_urls

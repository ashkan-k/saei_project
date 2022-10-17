from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/polls/', PollListView.as_view(), name='polls-list'),
    path('dashboard/polls/create/', PollCreateView.as_view(), name='polls-create'),
    path('dashboard/polls/update/<int:pk>/', PollUpdateView.as_view(), name='polls-update'),
    path('dashboard/polls/delete/<int:pk>/', PollDeleteView.as_view(), name='polls-delete'),
]

urlpatterns += dashboard_urls

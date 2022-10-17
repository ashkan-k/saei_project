from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/polls/', PollListView.as_view(), name='polls-list'),
    path('dashboard/polls/create/', PollCreateView.as_view(), name='polls-create'),
    path('dashboard/polls/update/<int:pk>/', PollUpdateView.as_view(), name='polls-update'),
    path('dashboard/polls/delete/<int:pk>/', PollDeleteView.as_view(), name='polls-delete'),

    path('dashboard/polls/user/', UserPollListView.as_view(), name='user-polls-list'),
    path('dashboard/polls/user/update/<int:pk>/', UserPollUpdateView.as_view(), name='user-polls-update'),
    path('dashboard/polls/user/delete/<int:pk>/', UserPollDeleteView.as_view(), name='user-polls-delete'),
    path('dashboard/polls/user/create/<int:pk>/', UserPollCreateView.as_view(), name='user-polls-create'),
]

urlpatterns += dashboard_urls

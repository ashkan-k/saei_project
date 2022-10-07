from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/chats/', ChatMessageListView.as_view(), name='chats-list'),
    path('dashboard/chats/<int:pk>/', ChatMessageRoomView.as_view(), name='chats-room'),
    path('dashboard/chats/delete/<int:pk>/', ChatMessagesDeleteView.as_view(), name='chats-delete'),
]

urlpatterns += dashboard_urls

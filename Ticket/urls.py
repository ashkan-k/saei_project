from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/ticket-categories/', TicketCategoryListView.as_view(), name='ticket-categories-list'),
    path('dashboard/ticket-categories/create/', TicketCategoryCreateView.as_view(), name='ticket-categories-create'),
    path('dashboard/ticket-categories/update/<int:pk>/', TicketCategoryUpdateView.as_view(),
         name='ticket-categories-update'),
    path('dashboard/ticket-categories/delete/<int:pk>/', TicketCategoryDeleteView.as_view(),
         name='ticket-categories-delete'),

    path('dashboard/tickets/', TicketsListView.as_view(), name='tickets-list'),
    path('dashboard/tickets/create/', TicketsCreateView.as_view(), name='tickets-create'),
    path('dashboard/tickets/update/<int:pk>/', TicketsUpdateView.as_view(), name='tickets-update'),
    path('dashboard/tickets/delete/<int:pk>/', TicketsDeleteView.as_view(), name='tickets-delete'),

    path('dashboard/tickets/answers/<int:pk>/', TicketAnswersListView.as_view(), name='tickets-answers-list'),
    path('dashboard/tickets/answers/create/<int:pk>/', TicketAnswersCreateView.as_view(),
         name='tickets-answers-create'),
]

urlpatterns += dashboard_urls

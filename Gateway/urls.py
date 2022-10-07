from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', include('Gateway.zarinpal.urls')),

    path('dashboard/payments/', PaymentTransactionListView.as_view(), name='payments-list'),
]

from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/zarinpal/payment/link/', pay),
    path('zarinpal/callback/', verify),
]

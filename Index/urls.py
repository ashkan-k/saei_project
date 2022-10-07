from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('', Index.as_view(), name='index'),
    path('about-us', AboutUs.as_view(), name='about_us'),
]

urlpatterns += dashboard_urls

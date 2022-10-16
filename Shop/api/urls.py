from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("galleries", ProductImageVS, "api-galleries-list")
router.register("", ProductsVS, "api-products-list")

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/installments/', UserInstallmentListView.as_view(), name='installments-list'),
    path('dashboard/installments/create/', UserInstallmentCreateView.as_view(), name='installments-create'),
    path('dashboard/installments/update/<int:pk>/', UserInstallmentUpdateView.as_view(), name='installments-update'),
    path('dashboard/installments/delete/<int:pk>/', UserInstallmentDeleteView.as_view(), name='installments-delete'),

    path('dashboard/installments/items/', UserInstallmentPaymentsListView.as_view(), name='installments-items-list'),
    path('dashboard/installments/items/<int:pk>/', UserInstallmentPaymentsListView.as_view(),
         name='installments-items-list'),
    path('dashboard/installments/items/detail/<int:pk>/', UserInstallmentPaymentsDetailView.as_view(),
         name='installments-items-detail'),
    path('dashboard/installments/items/delete/<int:pk>/', UserInstallmentPaymentsDeleteView.as_view(),
         name='installments-items-delete'),

    path('dashboard/installments-items/gateway/<int:pk>', UserInstallmentPaymentsGatewayView.as_view(),
         name='installments-items-gateway'),
]

front_urls = [
    # path('teacher/register/', CourseRegisterView.as_view(), name='teacher-register'),
    # path('teacher/profile/', CourseProfileInfoView.as_view(), name='teacher-profile'),
]

urlpatterns += dashboard_urls
urlpatterns += front_urls

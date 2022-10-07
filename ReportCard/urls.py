from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/report-card/', ReportCardsListView.as_view(), name='report-card-list'),
    path('dashboard/report-card/create/', ReportCardsCreateView.as_view(), name='report-card-create'),
    path('dashboard/report-card/update/<int:pk>/', ReportCardsUpdateView.as_view(), name='report-card-update'),
    path('dashboard/report-card/delete/<int:pk>/', ReportCardsDeleteView.as_view(), name='report-card-delete'),
    path('dashboard/report-card/pdf/<int:pk>/', ReportCardsPDFView.as_view(), name='report-card-pdf'),
]

urlpatterns += dashboard_urls

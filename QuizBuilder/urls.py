from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/quizzes/', QuizzesListView.as_view(), name='quizzes-list'),
    path('dashboard/quizzes/<int:pk>/', QuizzesListView.as_view(), name='quizzes-list'),
    path('dashboard/quizzes/create/', QuizzesCreateView.as_view(), name='quizzes-create'),
    path('dashboard/quizzes/update/<int:pk>/', QuizzesUpdateView.as_view(), name='quizzes-update'),
    path('dashboard/quizzes/delete/<int:pk>/', QuizzesDeleteView.as_view(), name='quizzes-delete'),
    path('dashboard/quizzes/delete/<int:pk>/', QuizzesDeleteView.as_view(), name='quizzes-delete'),
    path('dashboard/quizzes/detail/<int:pk>/', QuizDetailView.as_view(), name='quizzes-detail'),
    path('dashboard/quizzes/form/<int:pk>/', QuizFormView.as_view(), name='quizzes-form'),

    path('dashboard/user-quizzes/', UserQuizListView.as_view(), name='user-quizzes-list'),
    path('dashboard/user-quizzes/<int:pk>/', UserQuizListView.as_view(), name='user-quizzes-list'),
    path('dashboard/user-quizzes/delete/<int:pk>/', UserQuizDeleteView.as_view(), name='user-quizzes-delete'),
]

urlpatterns += dashboard_urls

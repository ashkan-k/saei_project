from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("questions", QuizQuestionVS, "api-questions-list")
router.register("user-quiz", UserQuizVS, "api-user-quiz-list")
router.register("", QuizVS, "api-quiz-list")

urlpatterns = [
    path('', include(router.urls)),
]

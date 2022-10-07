from django.contrib import admin
from .models import *


admin.site.register(Quiz)
admin.site.register(QuizQuestionChoice)
admin.site.register(QuizQuestion)
admin.site.register(UserQuiz)
admin.site.register(UserQuizQuestionAnswer)
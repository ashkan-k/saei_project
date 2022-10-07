from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ACL.rest_mixin import RestPermissionMixin
from QuizBuilder.api.serializers import *
from QuizBuilder.mixins import FilterUserQuizzesQuerysetMixin
from QuizBuilder.models import QuizQuestion, QuizQuestionChoice
from rest_framework.decorators import action


class QuizQuestionVS(ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['quiz_list', 'quiz_create', 'quiz_edit', 'quiz_delete', 'quiz_change_status']
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

    def update(self, request, *args, **kwargs):
        if request.data.get('deleted_choices'):
            QuizQuestionChoice.objects.filter(
                id__in=request.data.get('deleted_choices')).delete()
        return super().update(request, *args, **kwargs)


class QuizVS(ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['quiz_list', 'quiz_create', 'quiz_edit', 'quiz_delete', 'quiz_change_status']
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @action(
        detail=True,
        methods=['get'],
        url_path='questions',
        serializer_class=QuizQuestionSerializer
    )
    def get_questions_api(self, request, pk):
        exam = self.get_object()
        serializer = self.get_serializer(exam.questions.all(), many=True)
        return Response(serializer.data)


class UserQuizVS(FilterUserQuizzesQuerysetMixin, ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['user_quiz_list', 'user_quiz_create', 'user_quiz_edit', 'user_quiz_delete', 'user_quiz_detail',
                   'user_quiz_change_status']
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permissions = ['user_quiz_list']
        elif self.action == 'create':
            self.permissions = ['user_quiz_create']
        elif self.action == 'retrieve':
            self.permissions = ['user_quiz_detail']
        elif self.action == 'update':
            self.permissions = ['user_quiz_edit']
        elif self.action == 'destroy':
            self.permissions = ['user_quiz_delete']

        return super().get_permissions()

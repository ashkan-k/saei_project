from ast import Pass
from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, FormView
from django.urls import reverse_lazy
from ACL.mixins import SuperUserRequiredMixin, PermissionMixin
# from .filters import QuizFilters
# from .filters import QuizFilters, QuizUserFilters
# from .forms import *
# from .helpers import COURSE_STATUS, COURSE_USER_STATUS
from .filters import QuizFilters, UserQuizFilters
from .forms import QuizForm, QuizChangeStatusForm, QuizAnswerForm, UserQuizChangeStatusForm
from .mixins import FilterQuizzesQuerysetMixin, CheckUerQuizExpireMixin, FilterUserQuizzesQuerysetMixin
from .models import *
from django.conf import settings
from django.contrib import messages


class QuizzesListView(PermissionMixin, FilterQuizzesQuerysetMixin, ListView):
    permissions = ['quiz_list']
    model = Quiz
    context_object_name = 'quizzes'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'quizzes/admin/quizzes/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['change_status_form'] = QuizChangeStatusForm()
        context['status_filter_items'] = [
            {"name": i[1], "id": i[0]} for i in QUIZ_STATUS.CHOICES]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('pk'):
            queryset = queryset.filter(class_item_id=self.kwargs.get('pk'))
        return QuizFilters(data=self.request.GET, queryset=queryset).qs


class QuizzesCreateView(PermissionMixin, CreateView):
    permissions = ['quiz_create']
    template_name = "quizzes/admin/quizzes/form.html"
    model = Quiz
    form_class = QuizForm

    def get_success_url(self):
        return reverse_lazy("quizzes-update", kwargs={'pk': self.object.id})


class QuizzesUpdateView(PermissionMixin, UpdateView):
    permissions = ['quiz_edit']
    template_name = "quizzes/admin/quizzes/form.html"
    model = Quiz
    form_class = QuizForm
    success_url = reverse_lazy("quizzes-list")


class QuizzesDeleteView(PermissionMixin, DeleteView):
    permissions = ['quiz_delete']
    model = Quiz
    template_name = 'quizzes/admin/quizzes/list.html'
    success_url = reverse_lazy("quizzes-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


class QuizDetailView(PermissionMixin, FilterQuizzesQuerysetMixin, DetailView):
    permissions = ['quiz_detail']
    template_name = "quizzes/admin/quizzes/detail.html"
    model = Quiz

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(status='open')
        return qs


class QuizFormView(PermissionMixin, CheckUerQuizExpireMixin, FormView):
    permissions = ['quiz_detail']
    template_name = "quizzes/admin/quizzes/quiz.html"
    model = Quiz
    form_class = QuizAnswerForm
    success_url = reverse_lazy('quizzes-list')

    @property
    def quiz_object(self):
        return get_object_or_404(Quiz, pk=self.kwargs.get('pk'), status='open')

    @property
    def get_user_quiz_answer_sheet(self):
        obj, _ = UserQuiz.objects.get_or_create(user=self.user, quiz=self.quiz_object)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['object'] = self.quiz_object

        user_answer_sheet = self.get_user_quiz_answer_sheet
        if not user_answer_sheet.start_time:
            user_answer_sheet.start_time = datetime.datetime.now()
            user_answer_sheet.save()
        context['user_answer_sheet'] = user_answer_sheet

        return context

    def post(self, request, *args, **kwargs):
        res = super().post(request, *args, **kwargs)
        if res:
            return res

        user_quiz_answer_sheet = self.get_user_quiz_answer_sheet
        user_quiz_answer_sheet.score = 0

        for item in request.POST.getlist('answers'):
            if item == '':
                continue
            question, choice = item.split(',')
            data = {
                'question': question,
                'answer': choice,
                'user_quiz': user_quiz_answer_sheet,
            }
            form = QuizAnswerForm(data)
            if not form.is_valid():
                context = self.get_context_data()
                context['form'] = form
            user_question = form.save()

            if user_question.answer.is_answer:
                user_quiz_answer_sheet.score += user_question.question.score

        user_quiz_answer_sheet.status = 'done'
        user_quiz_answer_sheet.save()

        messages.success(self.request, 'پاسخ های شما با موفقیت ثبت شد.')
        return redirect(self.success_url)


""" UserQUizAnswers """


class UserQuizListView(PermissionMixin, FilterUserQuizzesQuerysetMixin, ListView):
    permissions = ['user_quiz_list']
    model = UserQuiz
    context_object_name = 'user_quizzes'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'quizzes/admin/user_quizzes/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['change_status_form'] = UserQuizChangeStatusForm()
        context['status_filter_items'] = [
            {"name": i[1], "id": i[0]} for i in UserQuizChoice.CHOICES]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('pk'):
            queryset = queryset.filter(quiz_id=self.kwargs.get('pk'))
        return UserQuizFilters(data=self.request.GET, queryset=queryset).qs


class UserQuizDeleteView(PermissionMixin, DeleteView):
    permissions = ['user_quiz_delete']
    model = UserQuiz
    template_name = 'quizzes/admin/user_quizzes/list.html'
    success_url = reverse_lazy("user-quizzes-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp

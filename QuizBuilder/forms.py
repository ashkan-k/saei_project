from django import forms
from django.contrib.auth import get_user_model
from QuizBuilder.models import Quiz, UserQuizQuestionAnswer, UserQuiz

User = get_user_model()


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = '__all__'


class QuizChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': name})


class QuizAnswerForm(forms.ModelForm):
    class Meta:
        model = UserQuizQuestionAnswer
        fields = '__all__'


class UserQuizChangeStatusForm(forms.ModelForm):
    class Meta:
        model = UserQuiz
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': name})

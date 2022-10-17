from django import forms
from django.contrib.auth import get_user_model
from Poll.models import Poll, UserPoll
User = get_user_model()


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'


class UserPollCreateForm(forms.ModelForm):
    class Meta:
        model = UserPoll
        fields = '__all__'


class UserPollEditForm(forms.ModelForm):
    class Meta:
        model = UserPoll
        exclude = ['user', 'poll']

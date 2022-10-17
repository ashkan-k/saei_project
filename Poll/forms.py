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


class UserPollDetailForm(forms.ModelForm):
    class Meta:
        model = UserPoll
        exclude = ['user', 'poll']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True

from django import forms
from django.contrib.auth import get_user_model
from Poll.models import Poll
User = get_user_model()


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'

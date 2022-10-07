from django import forms
from django.contrib.auth import get_user_model

from Help.models import Help

User = get_user_model()


class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = '__all__'

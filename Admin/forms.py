from django import forms
from .models import *


class DashboardImageForm(forms.ModelForm):
    class Meta:
        model = DashboardImage
        fields = '__all__'

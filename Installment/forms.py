from django import forms
from Installment.models import *


class UserInstallmentForm(forms.ModelForm):
    class Meta:
        model = UserInstallment
        fields = '__all__'

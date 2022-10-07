from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

from Slider.models import Slider
from Ticket.models import Ticket, TicketCategory, TicketAnswer
from utils.validator import validate_file_size

User = get_user_model()


class TicketCategoryForm(forms.ModelForm):
    class Meta:
        model = TicketCategory
        fields = '__all__'


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['user', 'status']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', '')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        ticket = super().save(False)
        ticket.user = self.request.user
        ticket.save()
        return ticket


class TicketAnswerForm(forms.ModelForm):
    class Meta:
        model = TicketAnswer
        exclude = ['user', 'ticket']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', '')
        self.ticket = kwargs.pop('ticket', '')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        answer = super().save(False)
        answer.user = self.request.user
        answer.ticket = self.ticket
        answer.save()
        return answer

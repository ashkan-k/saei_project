from django import forms
from django.contrib.auth import get_user_model
from ReportCard.models import ReportCard
from Sms.helpers import send_sms
from Sms.sms_texts import SMS_TEXTS

User = get_user_model()


class ReportCardForm(forms.ModelForm):
    class Meta:
        model = ReportCard
        fields = '__all__'

    field_order = ['user', 'title', 'class_item', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(student_profile__isnull=False, is_staff=False)
        self.fields['type'].widget.attrs.update({'ng-model': 'data.type'})

    def save(self, commit=True):
        if not self.instance.pk:
            sms_text = SMS_TEXTS['report_card_message'].format(self.instance.user.full_name, self.instance.title)
            send_sms(self.instance.user.phone, sms_text)
        return super().save(commit)

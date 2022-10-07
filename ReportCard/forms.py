from django import forms
from django.contrib.auth import get_user_model
from ReportCard.models import ReportCard

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

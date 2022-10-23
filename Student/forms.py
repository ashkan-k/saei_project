from django import forms
from django.contrib.auth import get_user_model

from Student.models import Student
from utils.validator import mobile_regex

User = get_user_model()


class StudentForm(forms.ModelForm):
    parent_phone = forms.CharField(label="شماره موبایل والد", max_length=11, min_length=11, validators=[mobile_regex],required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'parent_phone', 'password', 'avatar', 'national_id', 'father_name',
                  'marital_status',
                  'education_level', 'grade', 'intro_method', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields.pop('password')
            self.fields['parent_phone'].initial = self.instance.student_profile.parent_phone

    def save(self, commit=True):
        password = self.cleaned_data.pop('password', None)
        instance = super().save(commit)
        if password:
            instance.set_password(password)
            instance.save()

        student_profile, _ = Student.objects.update_or_create(user=instance)
        student_profile.parent_phone = self.cleaned_data.get('parent_phone')
        student_profile.approve()

        return instance

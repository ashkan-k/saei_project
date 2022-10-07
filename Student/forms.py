from django import forms
from django.contrib.auth import get_user_model

from Student.models import Student

User = get_user_model()


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'password', 'avatar', 'national_id', 'father_name',
                  'marital_status',
                  'education_level', 'grade', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields.pop('password')

    def save(self, commit=True):
        password = self.cleaned_data.pop('password', None)
        instance = super().save(commit)
        if password:
            instance.set_password(password)
            instance.save()

        student_profile, _ = Student.objects.update_or_create(user=instance)
        student_profile.approve()

        return instance

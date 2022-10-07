from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from Course.models import Course, CourseUser

User = get_user_model()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def full_clean(self):
        print('bbbbbbbbbbbbbbbbbbbb')
        print(self.data.get("start_date"))

        return super().full_clean()


class CourseChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': name})


class CourseUserForm(forms.ModelForm):
    class Meta:
        model = CourseUser
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['start_date'].widget.attrs.update({'ng-model': 'start_date'})


    def clean(self):
        user = self.cleaned_data['user']
        course = self.cleaned_data['course']

        if CourseUser.objects.filter(user=user, course=course).exists():
            raise forms.ValidationError('این کاربر قبلا به دوره اضافه شده است!', code='course')

        return super().clean()


class CourseUserChangeStatusForm(forms.ModelForm):
    class Meta:
        model = CourseUser
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': name})

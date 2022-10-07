from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from Class.models import Class, ClassUser, ClassAttendance

User = get_user_model()


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

    def full_clean(self):
        start_time = self.data.get('start_time')
        end_time = self.data.get('end_time')
        self.data._mutable = True

        if start_time:
            self.data['start_time'] = start_time.replace('PM', '').replace('AM', '').strip()
        if end_time:
            self.data['end_time'] = end_time.replace('PM', '').replace('AM', '').strip()

        return super().full_clean()


class ClassChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': name})


class ClassUserForm(forms.ModelForm):
    class Meta:
        model = ClassUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_staff=False, teacher_profile__isnull=True)

    def clean(self):
        user = self.cleaned_data['user']
        class_item = self.cleaned_data['class_item']

        qs = ClassUser.objects.filter(user=user, class_item=class_item)
        if self.instance.pk:
            qs = qs.exclude(id=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('این کاربر قبلا به کلاس اضافه شده است!', code='class_item')

        return super().clean()


class ClassUserChangeStatusForm(forms.ModelForm):
    class Meta:
        model = ClassUser
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': name})


class ClassAttendanceForm(forms.ModelForm):
    class Meta:
        model = ClassAttendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': name})

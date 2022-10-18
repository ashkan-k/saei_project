from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MinLengthValidator, MaxLengthValidator, RegexValidator

from Teacher.models import Teacher, TeacherPayment, TeacherAttendance
from utils.validator import validate_file_size

User = get_user_model()


class TeacherForm(forms.ModelForm):
    resume_file = forms.FileField(label='فایل رزمه',
                                  help_text='لطفا فایل رزمه خود را در قالب یکی از پسوند های (jpg,png,txt,docx,doc,pdf) آپلود کنید.',
                                  validators=[
                                      FileExtensionValidator(['jpg', 'png', 'jpeg', 'txt', 'doc', 'docx', 'pdf']),
                                      validate_file_size
                                  ],
                                  required=True)

    bank_account_number = forms.CharField(
        required=True,
        max_length=256,
        help_text='مثال: ۰۱۵۶۳۵۳۰۱۱',
        label="شماره حساب بانکی",
        validators=[MinLengthValidator(8), MaxLengthValidator(16), RegexValidator(r"[\d۱۲۳۴۵۶۷۸۹۰]{6,18}")]
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'password', 'avatar', 'national_id', 'father_name',
                  'marital_status',
                  'education_level', 'grade', 'intro_method', 'address', 'resume_file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields.pop('password')
            self.fields['resume_file'].required = False
            self.fields['bank_account_number'].initial = self.instance.teacher_profile.bank_account_number
            self.fields['resume_file'].initial = self.instance.teacher_profile.resume_file

    def save(self, commit=True):
        teacher_profile_data = {
            'resume_file': self.cleaned_data.pop('resume_file', None),
            'bank_account_number': self.cleaned_data.pop('bank_account_number', None)
        }

        password = self.cleaned_data.pop('password', None)

        instance = super().save(commit)
        if password:
            instance.set_password(password)
            instance.save()

        teacher_profile, _ = Teacher.objects.update_or_create(user=self.instance)

        for key, value in teacher_profile_data.items():
            setattr(teacher_profile, key, value)

        teacher_profile.save()
        # teacher_profile.approve()

        return instance


class TeacherPaymentForm(forms.ModelForm):
    class Meta:
        model = TeacherPayment
        fields = '__all__'


class TeacherAttendanceForm(forms.ModelForm):
    class Meta:
        model = TeacherAttendance
        fields = '__all__'

from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

from Slider.models import Slider
from utils.validator import validate_file_size

User = get_user_model()


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'

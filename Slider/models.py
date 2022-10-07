from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from utils.models import CustomModel
from utils.validator import validate_file_size
from ACL.models import Role
from ACL.permissions import ROLE_CODES


def upload_image(instance, filename):
    path = 'sliders/' + slugify(instance.title, allow_unicode=True)
    return path + '/' + filename


###################################################################################

class Slider(CustomModel):
    title = models.CharField(verbose_name='عنوان', max_length=255)
    text = models.TextField(verbose_name='متن', max_length=255, null=True, blank=True)
    link = models.URLField(verbose_name='لینک', max_length=255, null=True)
    image = models.ImageField(
        verbose_name='عکس', upload_to=upload_image,
        validators=[validate_file_size]
    )

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title or '---'

    @property
    def get_image(self):
        return self.image.url if self.image else ''

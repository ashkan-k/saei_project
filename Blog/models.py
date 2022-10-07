from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from ACL.models import Role
from Class.models import Class
from utils.models import CustomModel
from utils.validator import validate_file_size

User = get_user_model()


def upload_image(instance, filename):
    path = 'blog/' + slugify(f"{instance.title}", allow_unicode=True)
    return path + '/' + filename


###################################################################################
class BlogCategory(CustomModel):
    title = models.CharField(verbose_name='عنوان', max_length=255)
    slug = models.SlugField(verbose_name='نامک (slug)', max_length=255, allow_unicode=True, null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی مقاله ها'

    def __str__(self):
        return self.title or '---'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, True)
        return super().save(*args, **kwargs)


class Blog(CustomModel):
    user = models.ForeignKey(verbose_name='نویسنده', to=User, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(verbose_name='دسته بندی', to=BlogCategory, on_delete=models.CASCADE,
                                 related_name='blogs', null=True, blank=True)
    title = models.CharField(verbose_name='عنوان', max_length=255)
    slug = models.SlugField(verbose_name='نامک (slug)', max_length=255, allow_unicode=True, null=True, blank=True)
    text = models.TextField(verbose_name='متن')
    image = models.ImageField(
        verbose_name='عکس', upload_to=upload_image,
        validators=[validate_file_size]
    )

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return f"{self.user}-{self.title}" or '---'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, True)
        return super().save(*args, **kwargs)

    @property
    def get_image(self):
        return self.image.url if self.image else ''


class BlogComment(CustomModel):
    user = models.ForeignKey(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='blog_comments')
    blog = models.ForeignKey(verbose_name='بلاگ', to=Blog, on_delete=models.CASCADE, related_name='blog_comments')
    text = models.TextField(verbose_name='متن', max_length=150)
    is_accept = models.BooleanField(verbose_name='آیا تایید شده است؟', default=False)

    class Meta:
        verbose_name = 'نظرات مقاله'
        verbose_name_plural = 'نظرات مقاله ها'

    def __str__(self):
        return f"{self.user}-{self.blog}" or '---'

    @property
    def get_status(self):
        return 'تایید شده' if self.is_accept else 'تایید نشده'

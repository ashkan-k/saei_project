from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from ACL.models import Role
from Class.models import Class
from utils.models import CustomModel
from utils.validator import validate_file_size

User = get_user_model()


def upload_image(instance, filename):
    path = 'shop/' + slugify(f"{instance.title}", allow_unicode=True)
    return path + '/' + filename

def upload_gallery_image(instance, filename):
    path = 'shop/galleries/' + slugify(f"{instance.product.title}", allow_unicode=True)
    return path + '/' + filename

###################################################################################

class Category(CustomModel):
    title = models.CharField(verbose_name='عنوان', max_length=255)
    slug = models.SlugField(verbose_name='نامک (slug)', max_length=255, allow_unicode=True, null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصول ها'

    def __str__(self):
        return self.title or '---'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, True)
        return super().save(*args, **kwargs)


class Product(CustomModel):
    title = models.CharField(verbose_name='عنوان', max_length=255)
    slug = models.SlugField(verbose_name='نامک (slug)', max_length=255, allow_unicode=True, null=True, blank=True)
    desc = models.TextField(verbose_name='توضیحات')
    amount = models.PositiveIntegerField(verbose_name='قیمت (تومان)')
    discount_amount = models.PositiveIntegerField(
        verbose_name='قیمت تخفیفی (تومان)', null=True, blank=True)
    image = models.ImageField(
        verbose_name='عکس', upload_to=upload_image,
        validators=[validate_file_size])

    category = models.ForeignKey(to=Category, verbose_name='دسته بندی', on_delete=models.CASCADE,
                                 related_name='products', null=True)

    file = models.ImageField(
        verbose_name='فایل', upload_to=upload_image,
        null=True, blank=True,
        help_text='این فیلد برای محصولاتی است که بصورت فایلی و دانلودی هستند. اگر محصول شما دانلودی نیست این قسمت را خالی بگذارید.')

    class Meta:
        verbose_name = 'محصول(خدمات) فروشی'
        verbose_name_plural = 'محصول(خدمات) فروشی ها'

    def __str__(self):
        return self.title or '---'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, True)
        return super().save(*args, **kwargs)

    @property
    def get_image(self):
        return self.image.url if self.image else ''

    @property
    def get_file(self):
        return self.file.url if self.file else ''


class ProductImage(CustomModel):
    image = models.ImageField(
        verbose_name='عکس', upload_to=upload_gallery_image,
        validators=[validate_file_size])

    product = models.ForeignKey(to=Product, verbose_name='محصول', on_delete=models.CASCADE,
                                related_name='images', null=True)

    class Meta:
        verbose_name = 'گالری تصاویر محصولات'
        verbose_name_plural = 'گالری تصاویر محصولات ها'

    def __str__(self):
        return self.product

    def get_image_url(self):
        return self.image.url if self.image else None


class UserProduct(CustomModel):
    user = models.ForeignKey(verbose_name='کاربر', to=User,
                             on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(
        verbose_name='محصول(خدمت)', to=Product, on_delete=models.CASCADE, related_name='users')
    pay_amount = models.PositiveIntegerField(
        verbose_name='مبلغ پرداختی', null=True, blank=True)
    status = models.BooleanField(verbose_name='وضعیت پرداخت', default=False)

    class Meta:
        verbose_name = 'محصولات کاربران'
        verbose_name_plural = 'محصولات کاربران ها'

    def __str__(self):
        return f"{self.user}-{self.product}" or '---'

    @property
    def get_status(self):
        return 'موفق' if self.status else 'ناموفق'

    @property
    def get_status_class(self):
        return 'success' if self.status else 'danger'

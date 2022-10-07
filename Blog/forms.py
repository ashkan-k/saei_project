from django import forms
from django.contrib.auth import get_user_model

from Blog.models import Blog, BlogCategory, BlogComment
from ReportCard.models import ReportCard

User = get_user_model()


class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', '')
        super().__init__(*args, **kwargs)
        self.fields['category'].required = True

    def save(self, commit=True):
        blog = super().save(False)
        blog.user = self.request.user
        blog.save()
        return blog


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        exclude = ['is_accept']

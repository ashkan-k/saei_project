from django import forms
from django.contrib.auth import get_user_model
from Shop.models import Product, Category

User = get_user_model()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

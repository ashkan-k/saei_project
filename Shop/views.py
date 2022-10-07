# from Subscription.models import Type
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
# from Subscription.models import Type
from User.forms import UserSimpleForm
from ACL.mixins import VerifiedUserMixin, AnonymousUserMixin, SuperUserRequiredMixin, PermissionMixin
from .filters import ProductFilters, UserProductFilters, CategoryFilters
from .forms import *
from .models import Product, UserProduct, Category
from django.conf import settings
from django.contrib import messages

""" Categories """


class CategoriesListView(PermissionMixin, ListView):
    permissions = ['category_list']
    model = Category
    context_object_name = 'categories'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'shop/admin/categories/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return CategoryFilters(data=self.request.GET, queryset=queryset).qs


class CategoriesCreateView(PermissionMixin, CreateView):
    permissions = ['category_create']
    template_name = "shop/admin/categories/form.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("categories-list")


class CategoriesUpdateView(PermissionMixin, UpdateView):
    permissions = ['category_create']
    template_name = "shop/admin/categories/form.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("categories-list")


class CategoriesDeleteView(PermissionMixin, DeleteView):
    permissions = ['category_delete']
    model = Category
    template_name = 'shop/admin/categories/list.html'
    success_url = reverse_lazy("categories-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Products """


class ProductsListView(PermissionMixin, ListView):
    permissions = ['product_list']
    model = Product
    context_object_name = 'products'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'shop/admin/products/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return ProductFilters(data=self.request.GET, queryset=queryset).qs

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({"category_filter_items": [{"id": i.id, "name": i.title} for i in Category.objects.all()]})
        return super(ProductsListView, self).get_context_data(object_list=None, **kwargs)


class ProductsCreateView(PermissionMixin, CreateView):
    permissions = ['product_create']
    template_name = "shop/admin/products/form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products-list")


class ProductsUpdateView(PermissionMixin, UpdateView):
    permissions = ['product_create']
    template_name = "shop/admin/products/form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products-list")


class ProductsDeleteView(PermissionMixin, DeleteView):
    permissions = ['product_delete']
    model = Product
    template_name = 'shop/admin/products/list.html'
    success_url = reverse_lazy("products-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" User Products(sold products) """


class UserProductsListView(PermissionMixin, ListView):
    permissions = ['user_product_list']
    model = UserProduct
    context_object_name = 'user_products'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'shop/admin/user_products/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['status_filter_items'] = [
            {"name": i[1], "id": i[0]} for i in [('1', 'موفق'), ('0', 'ناموفق')]]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return UserProductFilters(data=self.request.GET, queryset=queryset).qs


class UserProductsDeleteView(PermissionMixin, DeleteView):
    permissions = ['user_product_delete']
    model = UserProduct
    template_name = 'shop/admin/products/list.html'
    success_url = reverse_lazy("user-products-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Front """


class Products(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'shop/front/product_user_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({'categories': Category.objects.all()})
        return super().get_context_data(object_list=None, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('slug'):
            queryset = queryset.filter(category__slug=self.kwargs.get('slug'))
        return ProductFilters(data=self.request.GET, queryset=queryset).qs


class ProductsDetail(DetailView):
    model = Product
    template_name = 'shop/front/product_user_detail.html'
    context_object_name = 'product_detail'
    slug_field = 'slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update(
            {'similar_products': Product.objects.filter(category=self.object.category).exclude(id=self.object.id)}
        )
        return super().get_context_data(object_list=None, **kwargs)

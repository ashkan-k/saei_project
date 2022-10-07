# from Subscription.models import Type
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, TemplateView
# from Subscription.models import Type
from User.forms import UserSimpleForm
from ACL.mixins import VerifiedUserMixin, AnonymousUserMixin, SuperUserRequiredMixin, PermissionMixin
from .filters import BlogFilters, BlogCategoryFilters, BlogCommentFilters
from .forms import *
from .models import Blog, BlogCategory, BlogComment
from django.conf import settings
from django.contrib import messages

""" Blog Category """


class BlogCategoryListView(PermissionMixin, ListView):
    permissions = ['blog_category_list']
    model = BlogCategory
    context_object_name = 'blogs'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'blogs/admin/categories/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return BlogCategoryFilters(data=self.request.GET, queryset=queryset).qs


class BlogCategoryCreateView(PermissionMixin, CreateView):
    permissions = ['blog_category_create']
    template_name = "blogs/admin/categories/form.html"
    model = BlogCategory
    form_class = BlogCategoryForm
    success_url = reverse_lazy("blog-categories-list")


class BlogCategoryUpdateView(PermissionMixin, UpdateView):
    permissions = ['blog_category_edit']
    template_name = "blogs/admin/categories/form.html"
    model = BlogCategory
    form_class = BlogCategoryForm
    success_url = reverse_lazy("blog-categories-list")


class BlogCategoryDeleteView(PermissionMixin, DeleteView):
    permissions = ['blog_category_delete']
    model = BlogCategory
    template_name = 'blogs/admin/categories/list.html'
    success_url = reverse_lazy("blog-categories-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Blog """


class BlogListView(PermissionMixin, ListView):
    permissions = ['blog_list']
    model = Blog
    context_object_name = 'blogs'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'blogs/admin/blogs/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return BlogFilters(data=self.request.GET, queryset=queryset).qs


class BlogCreateView(PermissionMixin, CreateView):
    permissions = ['blog_create']
    template_name = "blogs/admin/blogs/form.html"
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class BlogUpdateView(PermissionMixin, UpdateView):
    permissions = ['blog_edit']
    template_name = "blogs/admin/blogs/form.html"
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class BlogDeleteView(PermissionMixin, DeleteView):
    permissions = ['blog_delete']
    model = Blog
    template_name = 'blogs/admin/blogs/list.html'
    success_url = reverse_lazy("blog-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" BlogComment """


class BlogCommentListView(PermissionMixin, ListView):
    permissions = ['blog_comments_list']
    model = BlogComment
    context_object_name = 'comments'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'blogs/admin/comments/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return BlogCommentFilters(data=self.request.GET, queryset=queryset).qs


class BlogCommentDeleteView(PermissionMixin, DeleteView):
    permissions = ['blog_comments_delete']
    model = BlogComment
    template_name = 'blogs/admin/comments/list.html'
    success_url = reverse_lazy("blog-comments-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Front """


class Blogs(ListView):
    model = Blog
    context_object_name = 'blogs'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'blogs/front/blogs.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({'categories': BlogCategory.objects.all()})
        kwargs.update({'last_blogs': Blog.objects.order_by('-created_at')[:4]})
        return super().get_context_data(object_list=None, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('slug'):
            queryset = queryset.filter(category__slug=self.kwargs.get('slug'))

        search = self.request.GET.get('search')
        if search:
            q = Q(title__icontains=search) | Q(text__icontains=search)
            queryset = queryset.filter(q)
        return BlogFilters(data=self.request.GET, queryset=queryset).qs


class BlogDetail(DetailView):
    model = Blog
    slug_field = 'slug'
    queryset = Blog.objects.all()
    template_name = 'blogs/front/blogs-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({'categories': BlogCategory.objects.all()})
        kwargs.update(
            {'comments': BlogComment.objects.filter(is_accept=True, blog=self.object).order_by('-created_at')})
        return super().get_context_data(object_list=None, **kwargs)


class BlogCommentCreate(VerifiedUserMixin, CreateView):
    model = BlogComment
    form_class = BlogCommentForm
    template_name = 'blogs/front/blogs-detail.html'

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['user'] = request.user
        messages.success(request, 'نظر شما با موفقیت ثبت شد و پس از تایید توسط مدیر نمایش داده خواهد شد.')

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        self.success_url = self.request.GET.get('next_url', '/')
        return super().get_success_url()

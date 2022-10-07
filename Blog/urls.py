from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/blog/categories/', BlogCategoryListView.as_view(), name='blog-categories-list'),
    path('dashboard/blog/categories/create/', BlogCategoryCreateView.as_view(), name='blog-categories-create'),
    path('dashboard/blog/categories/update/<int:pk>/', BlogCategoryUpdateView.as_view(), name='blog-categories-update'),
    path('dashboard/blog/categories/delete/<int:pk>/', BlogCategoryDeleteView.as_view(), name='blog-categories-delete'),

    path('dashboard/blog/', BlogListView.as_view(), name='blog-list'),
    path('dashboard/blog/create/', BlogCreateView.as_view(), name='blog-create'),
    path('dashboard/blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
    path('dashboard/blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),

    path('dashboard/blog/comments/', BlogCommentListView.as_view(), name='blog-comments-list'),
    path('dashboard/blog/comments/delete/<int:pk>/', BlogCommentDeleteView.as_view(), name='blog-comments-delete'),
]

front_urls = [
    path('blogs/', Blogs.as_view(), name='blogs'),
    path('blogs/<str:slug>/', BlogDetail.as_view(), name='blogs-detail'),
    path('blogs/categories/<str:slug>/', Blogs.as_view(), name='category-blogs'),

    path('blogs/comments/create/', BlogCommentCreate.as_view(), name='blogs-comments-create'),
]

urlpatterns += dashboard_urls
urlpatterns += front_urls

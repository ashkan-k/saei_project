from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from Blog.api.serializers import *
from Blog.models import BlogComment


class BlogCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

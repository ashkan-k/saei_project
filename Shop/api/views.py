from Shop.api.serializers import *
from Shop.models import ProductImage, Product
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ProductsVS(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]

    @action(
        methods=["get"],
        url_name="gallery",
        detail=True,
        url_path="images/gallery",
        serializer_class=ProductImageSerializer,
    )
    def images_gallery(self, request, pk):
        objects = self.get_object().images.all()
        serializer = self.serializer_class(objects, many=True)

        return Response({'data': serializer.data}, 200)


class ProductImageVS(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminUser]

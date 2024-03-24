from rest_framework import viewsets

from digishop.apps.catalog.models import Category
from digishop.apps.catalog.serializers.front import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = CategorySerializer
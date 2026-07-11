from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsCategoryOwner


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer

    permission_classes = [
        IsAuthenticated,
        IsCategoryOwner,
    ]

    def get_queryset(self):

        return Category.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )
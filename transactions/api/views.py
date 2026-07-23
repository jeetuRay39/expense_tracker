from rest_framework import viewsets
from .serializers import TransactioinSerializer
from transactions.models import Transaction
from django_filters.rest_framework import DjangoFilterBackend

from transactions.api.filters import TransactionFilter

from rest_framework.permissions import IsAuthenticated


class TransactionViewSet(viewsets.ModelViewSet):

    serializer_class = TransactioinSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter


    def get_queryset(self):
        
        return Transaction.objects.filter(
            user = self.request.user
        ).select_related("category")
    
    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
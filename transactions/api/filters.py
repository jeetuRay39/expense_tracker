import django_filters
from transactions.models import Transaction


class TransactionFilter(django_filters.FilterSet):



    start_date = django_filters.DateFilter(
        field_name = "transaction_date",
        lookup_expr= "gte"
    )

    end_date = django_filters.DateFilter(
        field_name = "transaction_date",
        lookup_expr= "lte"
    )

    min_amount = django_filters.NumberFilter(
        field_name = "amount",
        lookup_expr= "gte"
    )
    max_amount = django_filters.NumberFilter(
        field_name = "amount",
        lookup_expr= "lte"
    )

    class Meta:
        model =  Transaction
        fields = [
            "transaction_type",
            "category"
        ]
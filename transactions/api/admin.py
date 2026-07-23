from django.contrib import admin
from transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "user",
        "category",
        "transaction_type",
        "amount",
        "transaction_date",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "transaction_type",
        "category",
    )
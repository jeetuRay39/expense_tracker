from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

class Transaction(models.Model):

    TRANSACTION_TYPES = (
        ("Income", "Income"),
        ("Expense", "Expense"),
    )

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name= "transactions"
    )

    category = models.ForeignKey(
        Category,
        on_delete= models.CASCADE,
        related_name= "transactions"

    )

    transaction_type = models.CharField(
        max_length=20,
        choices= TRANSACTION_TYPES
    )

    title = models.CharField(max_length=200)

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    note =  models.TextField(
        blank=True,
        null = True
    )
    
    transaction_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add= True
    )
    
    updated_at = models.DateTimeField(
        auto_now= True
    )

    class Meta: 
        ordering = ["-transaction_date"]

    def __str__(self):
        return self.title



    

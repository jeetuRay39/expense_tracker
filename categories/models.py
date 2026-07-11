from django.db import models
from django.conf import settings


class Category(models.Model):

    CATEGORY_TYPES = (
        ("income", "Income"),
        ("expense", "Expense"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    name = models.CharField(max_length=100)

    type = models.CharField(
        max_length=10,
        choices=CATEGORY_TYPES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["user", "name", "type"],
                name="unique_category_per_user"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.user.email})"
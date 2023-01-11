from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=15,
        null = False,
        blank= False,
        unique=True,
    )


class Todo(models.Model):
    DEFAULT_STATE = False

    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
    )

    is_done = models.BooleanField(
        default=DEFAULT_STATE,
        null=False,
        blank=False,
    )

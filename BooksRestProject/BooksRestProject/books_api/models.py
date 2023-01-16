from django.db import models


class Book(models.Model):
    MAX_LEN_TITLE = 20
    MIN_PAGE_NUMB = 0
    DESCRIPTION_MAX_LEN = 100
    MAX_LEN_AUTHOR = 20

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        null=False,
        blank=False,
    )

    pages = models.IntegerField(
        default=MIN_PAGE_NUMB,
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        default='',
        null=False,
        blank=False,
    )

    author = models.CharField(
        max_length=MAX_LEN_AUTHOR,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = "book"

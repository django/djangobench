from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author')

class Author(models.Model):
    author = models.CharField(max_length=100)

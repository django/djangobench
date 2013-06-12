from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

class Author(models.Model):
    author = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

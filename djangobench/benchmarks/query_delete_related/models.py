from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

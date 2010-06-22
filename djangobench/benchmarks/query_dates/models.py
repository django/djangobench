from django.db import models
import datetime

class Book(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=datetime.datetime.now())

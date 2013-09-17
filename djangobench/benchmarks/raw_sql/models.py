from django.db import models

class OneField(models.Model):
    field1 = models.CharField(max_length=100)

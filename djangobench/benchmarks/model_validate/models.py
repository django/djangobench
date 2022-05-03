from django.core.exceptions  import ValidationError
from django.utils.translation import gettext_lazy as _

from django.db import models

def validate_title(title):
    if title != 'hi':
        raise ValidationError(
            _('%(title)s is not hi'),
            params={'title': title},
        )

class Book(models.Model):
    title = models.CharField(max_length=100, validators=[validate_title])
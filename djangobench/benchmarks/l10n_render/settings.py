import os

from djangobench.base_settings import *

USE_I18N = False
USE_L10N = True
TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
)
INSTALLED_APPS = ['l10n_render', 'django.contrib.auth', 'django.contrib.contenttypes']

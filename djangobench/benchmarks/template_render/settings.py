import os

from djangobench.base_settings import *

INSTALLED_APPS = ['template_render']
TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
)
ROOT_URLCONF = 'template_render.urls'

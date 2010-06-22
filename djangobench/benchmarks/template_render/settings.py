from unipath import FSPath as Path
from djangobench.base_settings import *

INSTALLED_APPS = ['template_render']
TEMPLATE_DIRS = [Path(__file__).parent.child('templates').absolute()]
ROOT_URLCONF = 'template_render.urls'

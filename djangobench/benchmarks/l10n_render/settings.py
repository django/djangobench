from unipath import FSPath as Path
from djangobench.base_settings import *

USE_I18N = False
USE_L10N = True

TEMPLATE_DIRS = [Path(__file__).parent.child('templates').absolute()]
INSTALLED_APPS = ['l10n_render']

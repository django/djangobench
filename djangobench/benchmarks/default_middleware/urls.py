from django.conf.urls.defaults import *

urlpatterns = patterns('default_middleware',
    (r'^.*$', 'views.index'),
)

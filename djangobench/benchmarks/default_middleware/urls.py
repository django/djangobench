from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^.*$', 'views.index'),
)

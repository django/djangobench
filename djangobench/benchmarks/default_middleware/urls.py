try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from .views import index

urlpatterns = [
    url(r'^.*$', index),
]

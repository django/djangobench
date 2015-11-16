try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from .views import join, login, logout


urlpatterns = [
    url(r'/join/?$', join, name='join'),
    url(r'/login/?$', login, name='login'),
    url(r'/logout/?$', logout, name='logout'),
]

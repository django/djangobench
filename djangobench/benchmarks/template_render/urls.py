import django

from .views import join, login, logout

if django.VERSION >= (2, 0):
    from django.urls import re_path
elif django.VERSION >= (1, 4):
    from django.conf.urls import url as re_path
else:
    from django.conf.urls.defaults import url as re_path


urlpatterns = [
    re_path(r'/join/?$', join, name='join'),
    re_path(r'/login/?$', login, name='login'),
    re_path(r'/logout/?$', logout, name='logout'),
]

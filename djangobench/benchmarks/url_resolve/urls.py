import django

from . import views

if django.VERSION >= (2, 0):
    from django.urls import re_path
elif django.VERSION >= (1, 4):
    from django.conf.urls import url as re_path
else:
    from django.conf.urls.defaults import url as re_path


def generate_filler_patterns(num=1):
    """ Returns a list of url pattern inputs for garbage views """
    for n in range(num):
        yield re_path(r''.join((r'^', r'x' * 3 * n, r'/$')), views.basic)

urlpatterns = list(generate_filler_patterns(10))
urlpatterns.append(re_path(r'^basic/$', views.basic, name='basic'))
urlpatterns.append(re_path(r'^[a-z]*/$', views.catchall, name='catchall'))
urlpatterns.append(re_path(r'^replace/(?P<var>.*?)', views.vars, name='vars'))

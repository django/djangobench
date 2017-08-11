from django.conf.urls import url

from . import views


def generate_filler_patterns(num=1):
    """ Returns a list of url pattern inputs for garbage views """
    for n in range(num):
        yield url(r''.join((r'^', r'x' * 3 * n, r'/$')), views.basic)

urlpatterns = list(generate_filler_patterns(10))
urlpatterns.append(url(r'^basic/$', views.basic, name='basic'))
urlpatterns.append(url(r'^[a-z]*/$', views.catchall, name='catchall'))
urlpatterns.append(url(r'^replace/(?P<var>.*?)', views.vars, name='vars'))

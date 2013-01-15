try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('template_render.views',
    url(r'/join/?$', 'join', name='join'),
    url(r'/login/?$', 'login', name='login'),
    url(r'/logout/?$', 'logout', name='logout'),
)

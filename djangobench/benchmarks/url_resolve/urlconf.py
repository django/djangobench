from django.conf.urls.defaults import *

def generate_filler_patterns(num=1):
    """ Returns a list of url pattern inputs for garbage views """
    for n in range(num):
        yield (r''.join((r'^', r'x'*3*n, r'/$')), str(n))

patterns_input = ['']
patterns_input += generate_filler_patterns(10)
patterns_input.append((r'^basic/$', 'url_resolve.views.basic'))
patterns_input.append((r'^[a-z]*/$', 'url_resolve.views.catchall'))
patterns_input.append((r'^replace/(?P<var>.*?)', 'url_resolve.views.vars'))


urlpatterns = patterns(*patterns_input)

from django.conf.urls.defaults import patterns, include, url

def ok_view(request, *a, **kw):
    pass

def handler500(request):
    pass

sections = ["section%d" % i for i in range(10)]
features = ["feature%d" % i for i in range(20)]

urlpatterns = patterns('', *[
    url("^%s/%s$" % (s, f), ok_view) for s in sections for f in features
])

urlpatterns += patterns('', *[
    url("^(?P<locale>en|ru)/%s$" % f, ok_view)
        for s in sections for f in features
])

urlpatterns += patterns('', *[
    url("^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, ok_view) for f in features
])

# Total: 420 patterns

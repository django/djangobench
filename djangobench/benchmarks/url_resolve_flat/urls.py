try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

def ok_view(request, *a, **kw):
    pass

def handler404(request):
    pass

sections = ["section%d" % i for i in range(10)]
features = ["feature%d" % i for i in range(20)]

urlpatterns = [
    url("^%s/%s$" % (s, f), ok_view) for s in sections for f in features
]

urlpatterns += [
    url("^(?P<locale>en|ru)/%s$" % f, ok_view) for f in features
]

urlpatterns += [
    url("^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, ok_view) for f in features
]

# Total: 240 patterns

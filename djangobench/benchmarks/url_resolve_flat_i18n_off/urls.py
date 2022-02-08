import django
from django.http import HttpResponse

if django.VERSION >= (2, 0):
    from django.urls import re_path
elif django.VERSION >= (1, 4):
    from django.conf.urls import url as re_path
else:
    from django.conf.urls.defaults import url as re_path

def ok_view(request, *a, **kw):
    return HttpResponse()

def handler404(request):
    return HttpResponse()

sections = ["section%d" % i for i in range(10)]
features = ["feature%d" % i for i in range(20)]

urlpatterns = [
    re_path("^%s/%s$" % (s, f), ok_view) for s in sections for f in features
]

urlpatterns += [
    re_path(r"^(?P<locale>en|ru)/%s$" % f, ok_view) for f in features
]

urlpatterns += [
    re_path(r"^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, ok_view) for f in features
]

# Total: 240 patterns

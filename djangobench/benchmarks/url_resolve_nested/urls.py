import string

import django
from django.http import HttpResponse

if django.VERSION >= (2, 0):
    from django.urls import include, re_path
elif django.VERSION >= (1, 4):
    from django.conf.urls import include, url as re_path
else:
    from django.conf.urls.defaults import include, url as re_path


def ok_view(request, *a, **kw):
    return HttpResponse()

def handler500(request):
    return HttpResponse()

leaf_patterns = [re_path(r"^leaf$", ok_view)]

def int2ascii(x, mod, alphabet=string.digits + string.ascii_letters):
    alphabet = alphabet[:mod]
    result = []
    while x:
        x, rem = divmod(x, mod)
        result.append(alphabet[rem])
    return (''.join(reversed(result))).rjust(1, alphabet[0])

def pattern_tree(parent, height, level):
    if height == 0:
        return leaf_patterns
    ids = [parent + int2ascii(i, level) for i in range(level)]
    return [re_path("^%s/" % id_, include(pattern_tree(id_, height - 1, level))) for id_ in ids]

urlpatterns = pattern_tree("", 8, 2)
# Total: 2**8 = 256 leafs, 511 nodes

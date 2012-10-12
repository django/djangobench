from django.conf.urls.defaults import patterns, include, url
import string

def ok_view(request, *a, **kw):
    pass

def handler500(request):
    pass

leaf_patterns = patterns('', url(r"^leaf$", ok_view))

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
    return patterns('',
       *(url("^%s/" % id_, include(pattern_tree(id_, height-1, level)))
         for id_ in ids)
    )

urlpatterns = pattern_tree("", 8, 2)
# Total: 2**8 = 256 leafs, 511 nodes

from django import VERSION
from django.shortcuts import render_to_response

from djangobench.utils import run_benchmark

#set up some vars
objects1 = [object(), object(), object(), object(), object()]
objects2 = [object(), object(), object(), object(), object()]
object1 = object()
object2 = object()
object3 = None
num1 = 1
num2 = 2
boolean1 = True
SCRIPT_CONTENT_URL = '/some/prefix'
WEBSITE_DOMAIN = 'http://www.somedomain.com'
SHOW_ALT_HEADER = 'True'

def benchmark_django_lte_13():
    context = {
        'objects1': objects1,
        'objects2': objects2,
        'object1': object1,
        'object2': object2,
        'object3': object3,
        'num1' : num1,
        'num2' : num2,
        'boolean1': boolean1,
        'SCRIPT_CONTENT_URL': SCRIPT_CONTENT_URL,
        'WEBSITE_DOMAIN': WEBSITE_DOMAIN,
        'SHOW_ALT_HEADER': SHOW_ALT_HEADER
    }
    render_to_response('permalink_django_lte_13.html', context)

def benchmark_django_gt_13():
    context = {
        'objects1': objects1,
        'objects2': objects2,
        'object1': object1,
        'object2': object2,
        'object3': object3,
        'num1' : num1,
        'num2' : num2,
        'boolean1': boolean1,
        'SCRIPT_CONTENT_URL': SCRIPT_CONTENT_URL,
        'WEBSITE_DOMAIN': WEBSITE_DOMAIN,
        'SHOW_ALT_HEADER': SHOW_ALT_HEADER,
        'base_template': 'base.html' if VERSION > (1, 5) else 'base_django_lte_15.html',
    }
    render_to_response('permalink.html', context)

run_benchmark(
    benchmark_django_gt_13 if VERSION > (1, 3) else benchmark_django_lte_13,
    migrate=False,
    meta={
        'description': ('Render a somewhat complex, fairly typical template '
                        '(including inheritance, reverse URL resolution, etc.).'),
    }
)

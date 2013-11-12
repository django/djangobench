from django.test import RequestFactory
from django.utils.translation import get_language_from_request

from djangobench.utils import run_benchmark


LANGUAGES = (
    # no language preference
    '',
    # a few known languages
    'af', 'ar', 'az', 'bg', 'be', 'bn', 'br', 'bs', 'ca', 'cs', 'cy', 'da',
    'en', 'en-gb',
    # a few generic languages (fr-fr -> fr)
    'fr-fr',
    'fy-nl',
    'nl-nl',
    'en-us',
    # one non-strict language (zh -> zh-?)
    'zh',
    # multiple preferences
    'en-us,en', 'nl-be,nl'
    # some invalid
    'INVALID', 'UNKNOWN', 'NONE', 'KLINGON',
)


def benchmark():
    for lang in LANGUAGES:
        request.META = {'HTTP_ACCEPT_LANGUAGE': lang}
        get_language_from_request(request)


def setup():
    global request
    rf = RequestFactory()
    request = rf.get('/')
    request.COOKIES = {}


run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'Raw speed of locale detecting',
    }
)

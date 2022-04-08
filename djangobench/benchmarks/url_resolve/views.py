from django.http import HttpResponse


def basic(request):
    return HttpResponse()

def catchall(request):
    return HttpResponse()

def vars(request, var=None):
    return HttpResponse()

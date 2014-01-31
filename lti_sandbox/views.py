from django.http import HttpResponse


def error(request):
    return HttpResponse('<html><head></head><body><h1>Authentication error.</h1></body></html>')

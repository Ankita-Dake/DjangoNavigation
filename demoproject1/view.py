from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1><a href="https://www.google.com" target=_blank > open Google</a>'
                        '</h1><h1><a href="https://www.gmail.com" target=_blank > open Gmail</a></h1>'
                        '<h1><a href="https://www.facebook.com" target=_blank > open Facebook</a></h1>'
                        '<h1><a href="https://www.yahoo.com" target=_blank > open yahoo</a></h1>')


def info(request):
    return HttpResponse("Hello ")


def home(request):
    return HttpResponse("Home page")

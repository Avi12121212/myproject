from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello Avinash")


def books(request):
    return render(request, "book.html")

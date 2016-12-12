from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the diary index.")

def base(request, qst=100):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % qst)

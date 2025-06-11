from django.shortcuts import render

from django.http import HttpResponse

def accounts(response):
    return HttpResponse("hello, this is account app")

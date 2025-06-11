from django.shortcuts import render

from django.http import HttpResponse

def home(response):
    return HttpResponse('Hello, i am django server')

def success_page(response):
    return HttpResponse('Hello, this is success page')
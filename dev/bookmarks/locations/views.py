from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.


class SimpleHelloWorld(View):
    """
    view that returns Hello World
    """
    def get(self, requests, *args, **kwargs):
        return HttpResponse('<h1>Hello World</h1>')
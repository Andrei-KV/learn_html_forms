from multiprocessing import context
from re import template
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def weather(request):
    template = loader.get_template('home.html')
    context = {
        'example_using_context': 'This is example of using context',
    }
    return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def home(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())


def about(request):
    return HttpResponse("This is about page.")


def contact(response):
    return HttpResponse("This is contact page.")


def blog(response):
    return HttpResponse("This is blog page.")

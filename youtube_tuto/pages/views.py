from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args,**krgs):
    return HttpResponse("<h1>Hello World</h1><a href='./admin/'>admin</a>")
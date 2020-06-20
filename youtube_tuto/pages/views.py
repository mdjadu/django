from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**krgs):
    # print(request.user)
    return HttpResponse("<h1>Hello World</h1><a href='./admin/'>admin</a>")

def render_view(request,*args,**krgs):
    passing_data = {
        "text":"something that i like to pass",
        "number":117,
        "list":[23,56,741852963,"abc"]
    }
    return render(request,"index.html",passing_data)

# def 
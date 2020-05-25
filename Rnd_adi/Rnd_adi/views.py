from django.shortcuts import render
import request
from subprocess import run,PIPE
import sys

def button(request):
    return render(request,'index.html')

def external(request):
    inp = request.POST.get('inp') 
    out = run(sys.executable,['hello.py',inp],shell=False,stdout=PIPE)

    print(out)
    return render(request,'index.html',{'data1'})
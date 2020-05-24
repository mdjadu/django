from django.shortcuts import render

# Create your views here.
if request.method == 'POST' and 'run_script' in request.POST:

    # import function to run
    from .py_code.hello.py import *

    # call function
    def print_some (): 

    # return user to required page
        return HttpResponseRedirect(reverse("adi"))
from django.shortcuts import render
from .models import Product
from .form import ProductForm,RawProductForm

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)


    # # this one way but majorly a wrong way 
    # context = {
    #     "title":obj.title,
    #     "description":obj.description,
    #     "price":obj.price
    # }

    context = {
        "object":obj
    }
    return render(request,"products/products_details.html",context)


def product_form_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form":form
    }

    return render(request,"products/product_form_view.html",context)

def product_new_form_view(request):
    # print(request.GET)
    # print(request.POST)

    if request.method == "POST":
        data = request.POST.get('title')
        print(data)
        # Product.objects.create(title=data)
    context = {}
    return render(request,"products/new_form.html",context)

def pure_django_form(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
        my_form = RawProductForm()
    context = {
        "form":my_form
    }
    return render(request,"products/pure_django.html",context)
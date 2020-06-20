from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label='Title you like',widget=forms.TextInput(attrs={
        "placeholder":"Your Title"
    }))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={
        "class":"new-class-name two",
        "row":20,
        "cols":200
    }))
    price = forms.DecimalField(initial=1999.99)
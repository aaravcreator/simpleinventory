from django import forms
from .models import Product, Order,Customer
from django_select2 import forms as s2forms


class Products(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        'title__icontain'
    ]

class Customers(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontain",
        "mobile_no__icontain"
    ]



class ProductCreationForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
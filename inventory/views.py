from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import ProductCreationForm, OrderForm, CustomerForm


def home(request):
    products = Product.objects.all()
    order = Order.objects.all()
    order_count = Order.objects.all().count()
    order_completed = Order.objects.filter(order_status='completed').count()
    order_pending = Order.objects.filter(order_status='pending').count()
    customers = Customer.objects.all()
    customer_count = customers.count()
    
    orderform = OrderForm()
    if request.method == 'POST':
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            orderform.save()
            return redirect('/')
    
    context = {
        'products': products,
        'orders':order,
        'order_count':order_count,
        'order_completed':order_completed,
        'order_pending':order_pending,
        'customers':customers,
        'customer_count':customer_count,
        'orderform':orderform,
        
    }

    return render(request,'inventory/dashboard.html',context)

def add_order(request):
    orderform = OrderForm()
    if request.method == 'POST':
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            orderform.save()
            return redirect('/')
    context = {
        'orderform': orderform,
    }
    return render(request, 'inventory/customerorder.html',context)

def update_order(request,order_id):
    order = Order.objects.get(id=order_id)
    orderform = OrderForm(instance = order)
    if request.method == 'POST':
        orderform = OrderForm(request.POST,instance= order)
        if orderform.is_valid():
            orderform.save()
            return redirect('/')
    context = {
        'orderform':orderform
    }
    return render(request,'inventory/updateorder.html',context)


def addproduct_view(request):
    if request.user.is_authenticated:
        print('user is :'+str(request.user))

        product_form = ProductCreationForm()
        if request.method == 'POST':
            product_form = ProductCreationForm(request.POST)
            if product_form.is_valid():
                product_form.save()
                return redirect('/')
        context = {'form': product_form}
        return render(request,'inventory/products.html',context )
    return redirect('/')

def addcustomer(request):
    customerform = CustomerForm()
    context = {
        'customerform':customerform,
    }
    return render(request, 'inventory/addcustomer.html',context)

def customer_view(request,cust_id):
    customer = Customer.objects.get(pk=cust_id)
    order = customer.order_set.all()
    orderk = customer.order_set.all()
    for orderkk in orderk:
        print(orderkk.order_status)
        for order_items in orderkk.product.all():
            print(order_items.title)
            print(order_items.getprice()) 
        
    order_count = order.count()
    data = {
        'customer': customer,
        'order': order,
        'order_count':order_count
    }
    return render(request,'inventory/customer.html',data)

def test_view(request):
    return render(request,'inventory/test.html')


from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def home(request):

    orders  = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()

    total_delivered = orders.filter(status='Delivered').count()
    total_pending = orders.filter(status='pending').count()

    context = {'orders': orders,'customers': customers,'total_orders':total_orders,'total_delivered':total_delivered,'total_pending':total_pending}
    return render(request, 'accounts/dashboard.html',context)


def products(request):
    products = Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)   

    orders = customer.order_set.all() #will load the orders by customer
    orders_count = orders.count()
    context = {'customer':customer,'orders':orders,'orders_count':orders_count}
    return render(request,'accounts/customer.html',context)


# Create your views here.


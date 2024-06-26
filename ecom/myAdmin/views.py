
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'admin_dashboard/index.html')

def admin_product(request):
    return render(request,'admin_dashboard/products.html')

def admin_account(request):
    return render(request,'admin_dashboard/accounts.html')
    # return HttpResponse('')
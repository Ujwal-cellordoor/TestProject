
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name = 'dashboard'),
   path('products', views.admin_product, name = 'product'),
   path('accounts', views.admin_account, name = 'accounts'),
]

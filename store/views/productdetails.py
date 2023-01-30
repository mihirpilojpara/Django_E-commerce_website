from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from django.views import View


class ProductDetailsView(View):


    def get(self, request):
        products = Product.get_all_products()
        return render(request, 'productdetails.html', {'products': products})
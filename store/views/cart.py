from django.shortcuts import render, redirect,HttpResponseRedirect

from store.models.product import Product
from store.models.customer import Customer
from store.models.orders import Order
from django.views import View
from .checkout import Checkout

class Cart(View):
    def get(self, request):
        ids = None
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        return render(request, 'cart.html', {'products': products})

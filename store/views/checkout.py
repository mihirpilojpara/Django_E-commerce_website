from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from django.views import View


class Checkout(View):
    def post(self, request):
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))

        for product in products:
            print(str(product.id))
            order = Order(customer=Customer(id=customer),
                          product =product,
                          price=product.price,
                          address=address,
                          phonenumber=phonenumber,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')

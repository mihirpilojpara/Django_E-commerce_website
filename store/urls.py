"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from store.views import index, signin, login, category
from .views.index import Index
from .views.login import Login, logout
from .views.signin import Signin
from .views.category import Categories
from .views.cart import Cart
from .views.checkout import Checkout
from .views.orders import OrderView
from .views.productdetails import ProductDetailsView
from .views.profile import Profile
from .views.searchview import SearchView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signin', Signin.as_view()),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('category', auth_middleware(Categories.as_view()), name='categorypage'),
    path('productdetails', auth_middleware(ProductDetailsView.as_view()), name='productdetails'),
    path('search', SearchView.as_view(), name='search'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('checkout', auth_middleware(Checkout.as_view()), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='order'),
    path('userprofile', Profile.as_view(), name='profile')
]

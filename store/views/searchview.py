from django.shortcuts import redirect,render,HttpResponse
from django.views import View
from store.models.product import Product

class SearchView(View):
    def get(self, request):
        query = request.GET.get('query')

        if query:
            products = Product.get_all_product_by_categoryname(query)

            return render(request, 'search.html', {'product':products})
from store.models.customer import Customer
from django.shortcuts import redirect,render,HttpResponse
from django.views import View


class Profile(View):
    def get(self, request):
        customer = str(request.session.get('customer'))
        customer_profile = Customer.get_customer_id(customer)
        return render(request, 'profile.html', {'customers' : customer_profile})

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phonenumber = postData.get('phonenumber')
        error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phonenumber=phonenumber)

        error_message = self.validateCustomer(customer)

        if not error_message:

            customers = str(request.session.get('customer'))
            customer_profile = Customer.get_customer_id(customers)
            customer.save()
            return render(request, 'profile.html', {'customers': customer_profile})
        else:

            customer = str(request.session.get('customer'))
            customer_profile = Customer.get_customer_id(customer)
            data = {
                'error': error_message,
                'customers': customer_profile
                     }
            return render(request, 'profile.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phonenumber:
            error_message = 'Phone Number required'
        elif len(customer.phonenumber) < 10:
            error_message = 'Phone Number must be 10 char Long'

        return error_message

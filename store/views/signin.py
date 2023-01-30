from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signin(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phonenumber = postData.get('phonenumber')
        email = postData.get('email')
        password = postData.get('registerpassword')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phonenumber': phonenumber,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phonenumber=phonenumber,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        if not error_message:
            Success_message = 'Your account created successful, You Can now login'
            customer.password = make_password(customer.password)
            customer.register()

            data = {'success': Success_message}
            return render(request, 'login.html', data)
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signin.html', data)

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
        elif len(customer.password) < 6 :
            error_message = 'please enter more then 6 char'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message



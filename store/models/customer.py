from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    Active = models.BooleanField(default=False)


    def register(self):
        self.save()



    @staticmethod
    def get_customer_id(id):
        return Customer.objects.filter(id=id)


    @staticmethod
    def get_customer_name(first_name):
        return Customer.objects.get(username=first_name)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False

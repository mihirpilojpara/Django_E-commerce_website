from django import template
from store.models.customer import Customer

register = template.Library()


@register.filter(name='currency')
def currency(number):
    return '₹ ' + str(number)


@register.filter(name='multiply')
def price_product(number, number1):
    return number * number1


@register.filter()
def class_name(value):
    return value.__class__.__name__
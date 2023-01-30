from django import template
from store.models.customer import Customer

register = template.Library()


@register.filter()
def class_name(value):
    return value.__class__.__name__

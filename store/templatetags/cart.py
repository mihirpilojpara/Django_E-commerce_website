from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='price_product')
def price_product(product, cart):
    return product.price * cart_quantity(product, cart)


@register.filter(name='product_total_price')
def product_total_price(product, cart):
    sum = 0
    for p in product:
        sum += price_product(p, cart)
    return sum


@register.filter(name='gst_price')
def gst_price(product, cart):
    sum = 0
    for p in product:
        sum += price_product(p, cart)
    gst_total = sum * 0.18
    return gst_total


@register.filter(name='total_price')
def total_price(product, cart):
    sum = 0
    for p in product:
        sum += price_product(p, cart)
    gst = sum * 0.18

    total= gst + sum
    return total

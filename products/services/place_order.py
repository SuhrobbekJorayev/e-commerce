from products.models import Order
from rest_framework.exceptions import ValidationError


def place_order(product, customer, quantity):
    if product and customer and quantity > 0:
        order = Order.objects.create(
            product=product,
            customer=customer,
            quantity=quantity
        )
        return order
    else:
        raise ValidationError('Invalid order parameters.')

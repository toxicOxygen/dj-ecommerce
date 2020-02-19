from django import template
from orders.models import Order

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user,ordered=False)

        if qs.exists():
            order = qs[0]
            return order.get_item_count()


@register.filter
def cart_total_price(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user,ordered=False)

        if qs.exists():
            order = qs[0]
            return order.get_price_total()
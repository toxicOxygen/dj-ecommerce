from django.db import models
from items.models import Item
from django.contrib.auth import get_user_model

class OrderItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.item.title
    
    def get_order_item_total(self):
        if self.item.discount_price:
            return self.quantity * self.item.discount_price
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def get_item_count(self):
        return len(self.items.all())
    
    def get_price_total(self):
        total = 0.0
        for orderItem in self.items.all():
            total += orderItem.get_order_item_total()
        return total.__round__(2)

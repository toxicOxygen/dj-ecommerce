import uuid
from django.db import models
from django.urls import reverse

CATEGORIES = (
    ('S','Shirts'),
    ('OW','Outwear'),
    ('SW','Sports'),
    ('MJ',"Men's Jewelry"),
    ('F','Fashion'),
    ('W',"Watches")
)

LABELS = (
    ('N','New'),
)

class Item(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORIES,max_length=2)
    label = models.CharField(choices=LABELS,max_length=2,blank=True, null=True)
    image = models.ImageField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-detail',args=[str(self.pk),])
    
    def get_add_to_cart_url(self):
        return reverse('add_to_cart',args=[str(self.pk),])
    
    def get_remove_from_cart_url(self):
        return reverse('remove_from_cart',args=[str(self.pk),])

    def get_reduce_quantity_url(self):
        return reverse('remove_quantity',args=[str(self.pk),])

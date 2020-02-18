import uuid
from django.db import models
from django.urls import reverse

CATEGORIES = (
    ('S','shirts'),
    ('OW','Outwear'),
    ('SW','Sports')
)

class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField(editable=False,max_length=200,auto_created=True,unique=True)
    category = models.CharField(choices=CATEGORIES,max_length=2)
    image = models.ImageField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-detail',args=(str(self.slug)))

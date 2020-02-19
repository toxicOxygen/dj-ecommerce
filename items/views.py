from django.views.generic import ListView,DetailView
from .models import Item

class HomePageView(ListView):
    model = Item
    template_name = "items/home.html"
    context_object_name = "items"

class ItemDetailView(DetailView):
    model = Item
    template_name = "items/product_details.html"
    context_object_name = "item"
from django.views.generic import ListView,DetailView
from .models import Item

class HomePageView(ListView):
    model = Item
    template_name = "items/home.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "items/product-detail.html"
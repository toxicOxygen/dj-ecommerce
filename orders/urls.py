from django.urls import path
from .views import (
    add_item_to_cart,
    reduce_item_quantity,
    remove_item_from_cart,
    CartView
)

urlpatterns = [
    path('<uuid:pk>/add-to-cart/',add_item_to_cart,name="add_to_cart"),
    path('<uuid:pk>/remove-from-cart/',remove_item_from_cart,name="remove_from_cart"),
    path('<uuid:pk>/reduce-quantity/',reduce_item_quantity,name="remove_quantity"),
    path('cart',CartView.as_view(),name="cart")
]
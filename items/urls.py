from django.urls import path
from .views import HomePageView,ItemDetailView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('<str:slug>/',ItemDetailView.as_view(),name='product-detail')
]
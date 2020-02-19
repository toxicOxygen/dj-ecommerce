from django.urls import path
from .views import HomePageView,ItemDetailView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('<uuid:pk>/',ItemDetailView.as_view(),name='product-detail')
]
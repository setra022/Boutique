from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.DetailView.as_view(), name="detail"),
    path("add-to-cart", views.add_to_cart, name="add-to-cart"),
    path("cart", views.cart, name="cart")
]
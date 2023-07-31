from django.shortcuts import get_object_or_404, redirect
from .models import Article, Cart, Product
from django.views.generic import ListView, DetailView

# Create your views here.

class IndexView(ListView):
    model = Article


class DetailView(DetailView):
    model = Article


def add_to_cart(request):
    customer = request.user
    product_id = request.POST.get("product")
    product = get_object_or_404(Product, pk=product_id)
    cart, _ = Cart.objects.get_or_create(customer=customer)
    cart.add(product)

    return redirect("store:detail", product.article.id)


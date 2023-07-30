from .models import Article
from django.views.generic import ListView, DetailView

# Create your views here.

class IndexView(ListView):
    model = Article


class DetailView(DetailView):
    model = Article


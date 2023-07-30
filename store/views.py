from django.shortcuts import get_object_or_404, render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "store/index.html", context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {"article": article}
    return render(request, "store/detail.html", context)

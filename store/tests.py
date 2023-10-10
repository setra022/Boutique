from django.test import TestCase
from django.urls import reverse

from store.models import Article

# Create your tests here.
class ArticleModelTests(TestCase):

    def test_str_return_name(self):
        name = "Tshirt"
        article = Article(name=name)
        self.assertEqual(str(article), name)


class ArticleIndexViewTests(TestCase):

    def test_no_articles(self):
        response = self.client.get(reverse("store:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pas d'article disponible.")

    def test_create_article(self):
        article = Article.objects.create(name="Baskets")
        response = self.client.get(reverse("store:index"))
        self.assertQuerySetEqual(response.context["article_list"], [article])
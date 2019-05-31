from django.urls import include, path, reverse, resolve
from rest_framework.test import APITestCase, URLPatternsTestCase


class ApiURLsTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_authors_url(self):
        url = reverse('author-list')
        response = self.client.get(url, format='json')
        assert response.status_code == 200

    def test_book_url(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        assert response.status_code == 200


def test_authors_detail():
    url = reverse('author-detail', kwargs={'pk': 1})
    assert resolve(url).view_name == 'author-detail'


def test_book_detail():
    url = reverse('book-detail', kwargs={'pk': 1})
    assert resolve(url).view_name == 'book-detail'

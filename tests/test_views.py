import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAuthorView:

    def test_get(self):
        client = APIClient()
        url = reverse('author-detail', kwargs={'pk': 1})
        response = client.get(url, format='json')
        assert response.data == {
            'url': 'http://testserver/api/authors/1/', 'first_name': 'Рей', 'last_name': 'Бредбери'
        }

    def test_post(self):
        client = APIClient()
        url = reverse('author-list')
        content = {'first_name': 'TestName', 'last_name': 'TestLastname'}
        response = client.post(url, data=content, format='json')
        assert response.data == {
            {'url': 'http://testserver/api/authors/13/', 'first_name': 'TestName', 'last_name': 'TestLastname'}
        }

    def test_put(self):
        client = APIClient()
        url = reverse('author-detail', kwargs={'pk': 13})
        content = {'first_name': 'PutName', 'last_name': 'PutLastname'}
        response = client.put(url, data=content, format='json')
        assert response.data == {
            {'url': 'http://testserver/api/authors/13/', 'first_name': 'PutName', 'last_name': 'PutLastname'}
        }

    def test_delete(self):
        client = APIClient()
        url = reverse('author-detail', kwargs={'pk': 13})
        content = {'first_name': 'PutName', 'last_name': 'PutLastname'}
        response = client.delete(url, data=content, format='json')
        assert response.data == {"detail": "Не найдено."}


class TestBookView:

    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_put(self):
        pass

    def test_delete(self):
        pass
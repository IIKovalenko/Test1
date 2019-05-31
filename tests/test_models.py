from api.models import Author, Book

import pytest


@pytest.mark.django_db
class TestModels:

    def test_create_author(self):
        author = Author.objects.create(
            first_name='test_fname',
            last_name='test_lname',
        )
        assert author.first_name == 'test_fname' and author.last_name == 'test_lname'

    def test_create_book(self):
        book = Book.objects.create(
            title='test_title',

        )
        assert book.title == 'test_title'

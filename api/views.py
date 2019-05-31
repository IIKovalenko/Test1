from django.db.models import Count
from django.db.models.expressions import RawSQL
from rest_framework import viewsets

from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.annotate(num_books=Count('book')).order_by('-num_books')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    sql_ = """
            SELECT b.id, b.title 
            FROM "api_book" b 
            LEFT JOIN (
            SELECT aa.id, COUNT(*) AS cnt 
            FROM "api_book" bb 
            INNER JOIN "api_author" aa ON aa."id" = bb.author_id 
            GROUP BY aa.id, aa.last_name
            ) a ON a.id = b.author_id 
            ORDER BY a.cnt DESC
        """
    queryset = Book.objects.raw(sql_)
    serializer_class = BookSerializer

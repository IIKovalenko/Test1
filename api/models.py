from django.db import models


class Author(models.Model):

    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=40)

    class Meta:
        ordering = ['last_name']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        self.full_name = self.first_name + ' ' + self.last_name
        return self.full_name


class Book(models.Model):

    title = models.CharField('Наименование книги', max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, verbose_name='Автор')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

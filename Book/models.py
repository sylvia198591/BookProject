from datetime import date
from django.db import models
# Create your models here.
from django.db.models import CharField, IntegerField, ForeignKey,FloatField, CASCADE, ManyToManyField

# Model - Author, Fields - name, age
class Author(models.Model):
    name = CharField(max_length=100,null=True)
    age = IntegerField(null=True)
    auth_rate=FloatField(null=True)

    # class Meta:
    #     fields

    def __str__(self):
        return f'{self.id}'

# Model - Book, Fields - name, price, description, author(Author), genres(Genre)
class Book(models.Model):
    name = CharField(max_length=100)
    price = FloatField()
    description = CharField(max_length=200)
    author = ForeignKey(Author, on_delete=CASCADE, related_name='books')
    rating = IntegerField()
    isbn=CharField(max_length=25)
    pub_date = models.DateTimeField(default='2000-01-01 00:00:00')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'name: {self.name}, price: {self.price}, rating: {self.rating}'
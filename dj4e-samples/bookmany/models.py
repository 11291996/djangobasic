from django.db import models

#implementing many-to-many relationship where multiple elements in key column of relational database
class Book(models.Model):
    title = models.CharField(max_length=200)
    #through parameter represents the intermediate table that you want to use to represent the many-to-many relationship
    #using through table to represent many-to-many relationship
    #acutal data of authors is stored in the through table
    authors = models.ManyToManyField('Author', through='Authored') 

class Author(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField('Book', through='Authored')

#intermediate table to represent many-to-many relationship
class Authored(models.Model):
    #on delete cascade means that when a book is deleted, all the authors associated with that book will also be deleted in the through table
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

#one can add to the database using the python shell as well
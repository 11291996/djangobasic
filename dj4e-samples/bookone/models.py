from django.db import models

#basic one to many models
class Lang(models.Model):
    name = models.CharField(max_length=200) #simple model

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    lang = models.ForeignKey('Lang', on_delete=models.SET_NULL, null=True) #this starts the relational database
    #deleted table is set to null
    #since books can have no language

class Instance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE) #this is the second part of the relational database
    #this will delete the whole row if the relation is deleted
    due_back = models.DateField(null=True, blank=True)

#the migrations will link the models to the database
#one can also use Django shell to use the function and instances above and add data to the database
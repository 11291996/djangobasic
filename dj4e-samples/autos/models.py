from django.db import models
from django.core.validators import MinLengthValidator


class Make(models.Model):
    name = models.CharField(
            max_length=200, 
            help_text='Enter a make (e.g. Dodge)',
            validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    ) 

    def __str__(self): #connecting with pyton str function
        """String for representing the Model object."""
        return self.name


class Auto(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    #creates a positive integer field
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False) #making a foreign key

    # Shows up in the admin list
    def __str__(self):
        return self.nickname

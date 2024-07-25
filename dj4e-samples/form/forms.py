from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

#as models match data to the database, forms match data to the software of the server
#using forms is complex as they must be created, updated, and deleted
#from get requests, empty forms accept data
#then send post requests to validate the data
#then it fixes the data when it is invalid
#then it hands the data to the model 
#it redirects to the success page
#and get requests are sent to the success page
#and the data is displayed via view and template

#inherit from Django's built-in forms class
class BasicForm(forms.Form):
    title = forms.CharField(validators=[
        validators.MinLengthValidator(2, "Please enter 2 or more characters")]) #validators are used to check the data
    mileage = forms.IntegerField()
    purchase_date = forms.DateField()

from django.forms import ModelForm
from form.models import Cat

# Create the form class.
class CatForm(ModelForm):
    class Meta:
        model = Cat
        # fields = ['name', 'breed', 'comments']
        fields = '__all__'


# References 

# https://docs.djangoproject.com/en/3.0/ref/forms/api/
# https://docs.djangoproject.com/en/3.0/ref/forms/fields/#datefield
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#using-validation-in-practice
# https://docs.djangoproject.com/en/3.0/ref/validators/

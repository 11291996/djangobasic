from django.forms import ModelForm
from autos.models import Make


# Create the form class.
class MakeForm(ModelForm): #this form follows the models but it is not always the case
    #so it inherits from ModelForm
    class Meta:
        model = Make
        fields = '__all__'

from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


class Pic(models.Model):
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    #description of the picture
    text = models.TextField()
    #implements the login system
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Picture
    #the actual image file
    picture = models.BinaryField(null=True, blank=True, editable=True) 
    #the header of the image file for the browser to know how to display it
    content_type = models.CharField(max_length=256, null=True, blank=True, 
                                    help_text='The MIMEType of the file')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title

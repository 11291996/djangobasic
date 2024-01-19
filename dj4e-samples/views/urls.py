from django.urls import path
from . import views
from django.views.generic import TemplateView

#https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name='views'
urlpatterns = [
    #pre-defined class from Django
    #this leads to a folder 
    path('', TemplateView.as_view(template_name='views/main.html')),
    # function from views.py
    # executes the function when requests comes in as /view/function
    path('funky', views.funky),
    path('danger', views.danger),
    path('game', views.game),
    path('rest/<int:guess>', views.rest), #path parameter with type validation
    #str will take any non empty string
    #play with redirect
    path('bounce', views.bounce),
    # our class from views.py
    path('main', views.MainView.as_view()), #as_view() takes class' method as a python function
    path('remain/<slug:guess>', views.RestMainView.as_view()), 
    #slug takes strings consisting of ASCII letters or numbers, plus the hyphen and underscore characters.
    #uuid takes Universally Unique Identifier -> id created by the system
    #path takes any non empty string including slashes
]


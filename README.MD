after setting the environment 

make project by 

django-admin startproject projectname

the basic structure would be 

mysite/
    manage.py -> command line utility and controlled also with Admin API 
    mysite/
        __init__.py -> just a regular python init
        settings.py -> settings of this whole website
        urls.py -> URL dispatcher in Web Server, part of controller in Web Server
        asgi.py -> manages ASGI web requests
        wsgi.py -> manages WSGI web requests

setting.py can manage incoming clients -> see mysite setting.py
also time zone is managed in this file

python manage.py shell -> connect manage.py to shell

starting the server 
python manage.py check -> trying deploying without acutally deploying it
python manage.py runserver ip -> select ip default is localhost

Creating a database

select a query package, create a database in the upper mysite folder

python manage.py createsuperuser -> creates an access to manage the project via Admin API 

App -> an application for the web, it can be copied into many webs
Project -> collections of different apps

create an app

python manage.py startapp appname

the basic app structure would be 

appname/
    __init__.py
    admin.py -> used for registering the Django models into the Django administration
    apps.py -> application configuration
    migrations/
        __init__.py
    models.py -> does object relational mapping in Web Server #polls models.py
    tests.py -> tests the application 
    views.py -> can be both controller and view 

one can create urls.py in apps

Object relational mapping in django

python manage.py makemigration (appname) -> creates table structure for django
python manage.py sqlmigrate (appname) (migration number) -> shows SQL command in the migrations 
this is for frequent updates on models in django
python manage.py migrate -> creates table structure with django's for actual database
go to setting.py to control which database to create also which database to connect if it already exists

python manage.py dbshell -> checks connectivity

After these are set one can get http request from clients 

Django creates python objects from http request via class called HttpRequest
then the controller designed for the project returns an object from a class called HttpResponse

when it reaches the ip, the request is routed to HttpRequest class from Django and it is sent to the second project folder's urls.py, the start of the controller
then the controller will do its work and send HttpResponse to Django and it will send back http response

second project folder's urls.py sets the paths via django.urls's function called path -> see dj4e's urls.py

then http request can access the applications and its views.py

basic usage of view.py is shown in dj4e's views application's views.py

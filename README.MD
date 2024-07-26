# Django basic

## make project 

After setting the environment 

```bash
django-admin startproject projectname
```

the basic structure would be 
```markdown
mysite/
    manage.py -> command line utility and controlled also with Admin API 
    mysite/
        __init__.py -> just a regular python init
        settings.py -> settings of this whole website
        urls.py -> URL dispatcher in Web Server, part of controller in Web Server
        asgi.py -> manages ASGI web requests
        wsgi.py -> manages WSGI web requests
```

setting.py can manage incoming clients -> see mysite's setting.py
also time zone is managed in this file

```bash
python manage.py createsuperuser 
```
-> creates an access to manage the project via Admin API 

```bash
python manage.py shell 
```
-> connect manage.py to shell

## starting the server 
```bash
python manage.py check 
```
-> trying deploying without acutally deploying it
```bash
python manage.py runserver ip 
```
-> select ip default is localhost

App -> an application for the web, it can be copied into many webs \
Project -> collections of different apps

## create an app

```bash
python manage.py startapp appname
```

the basic app structure would be 
```markdown
appname/
    __init__.py
    admin.py -> used for registering the Django models into the Django administration
    apps.py -> application configuration
    migrations/
        __init__.py
    models.py -> does object relational mapping in Web Server #my site poll's models.py
    tests.py -> tests the application 
    views.py -> can be both controller and view 
```

one can create urls.py in apps

## creating a database

select a query package, create a database in the upper mysite folder

object relational mapping in django
```bash
python manage.py makemigration (appname) 
```
-> creates table structure for django
```bash
python manage.py sqlmigrate (appname) (migration number) 
```
-> shows SQL command in the migrations 
this is for frequent updates on models in django
```bash
python manage.py migrate 
```
-> creates table structure with django's for actual database

go to setting.py to control which database to create it 
also which database to connect if it already exists

```bash
python manage.py dbshell 
```
-> checks connectivity

### After these are set one can get http request from clients 

Django creates python objects from http request via class called HttpRequest
then the controller designed for the project returns an object from a class called HttpResponse

when it reaches the ip, the request is routed to HttpRequest class from Django and it is sent to the second project folder's urls.py, the start of the controller
then the controller will do its work and send HttpResponse to Django and it will send back http response

second project folder's urls.py sets the paths via django.urls's function called path -> see dj4e's urls.py

then http request can access the applications and its views.py

basic usage of view is shown in dj4e's views application

basic usage of template is shown in dj4e's tmpl application

basic URL mapping is shown in dj4e's route application 

basic generic view is shown in dj4e's gview application

basic form usage is shown in dj4e's getpost application

basic cookie and session usage is shown in dj4e's session application

basic model usage is shown in dj4e's bookone and scripts application

basic login and logout is shown in dj4e's authz and home application

more advanced form usage is shown in dj4e's form application

login, page and list creation features using the whole backend are done in dj4e's autos application
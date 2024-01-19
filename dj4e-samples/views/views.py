from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View

# Create your views here.
#just return this whatever request comes in
def funky(request):
    response = """<html><body><p>This is the funky function sample</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response)
#uses 'guess' data from the resquest and return response
#this kind of parameter is called a query, key, or value parameter
def danger(request) :
    response = """<html><body>
    <p>Your guess was """+request.GET['guess']+"""</p> 
    </body></html>"""
    return HttpResponse(response)
#uses 'guess' data but uses escape function manipulates the data disabling code generation
def game(request) :
    response = """<html><body>
    <p>Your guess was """+escape(request.GET['guess'])+"""</p>
    </body></html>"""
    return HttpResponse(response)
#this code gets data from urls.py itself. 
#this kind of parameter is called a path parameter
def rest(request, guess) :
    response = """<html><body>
    <p>Your guess was """+escape(guess)+"""</p>
    </body></html>"""
    return HttpResponse(response)

# This is a command to the browser
# Redirects the request into a new view 
def bounce(request) :
    return HttpResponseRedirect('https://www.dj4e.com/simple.htm')

#https://docs.djangoproject.com/en/3.0/topics/class-based-views/
#main is a class based view now oop can be applied for views
class MainView(View) :
    def get(self, request):
        response = """<html><body><p>Hello world MainView in HTML</p>
        <p>This sample code is available at
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></html>"""
        return HttpResponse(response)
#parameters on class
class RestMainView(View) :
    def get(self, request, guess):
        print("We got a slug from the URL", guess)
        response = """<html><body>
        <p>Your guess was """+escape(guess)+"""</p>
        </body></html>"""
        return HttpResponse(response)


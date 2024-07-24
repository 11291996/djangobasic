from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.http import urlencode

class OpenView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

class ApereoView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

#returning different views based on the login data
class ManualProtect(View) :
    def get(self, request):
        if not request.user.is_authenticated : #getting the user data from the request
            loginurl = reverse('login')+'?'+urlencode({'next': request.path}) #next is a path parameter used to redirect on certain conditions
            return redirect(loginurl)
        return render(request, 'authz/main.html')

#Django object that does the same thing
class ProtectView(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'authz/main.html')

from django.http import HttpResponse

class DumpPython(View) :
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        #get the user data from login
        resp += "Login url: " + reverse('login') + "\n" #use reverse to get the url and login data
        resp += "Logout url: " + reverse('logout') + "\n\n" #logout url will be different and limited than login url
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Email: " + req.user.email + "\n"
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/authz">Go back</a>"""
        return HttpResponse(resp)


# https://docs.djangoproject.com/en/3.0/topics/auth/default/#authentication-in-web-requests


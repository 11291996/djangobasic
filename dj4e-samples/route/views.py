from django.shortcuts import render
from django.urls import reverse
from django.views import View
#deals with request for first view
class FirstView(View):  
    def get(self, request) :
        return render(request, 'route/main.html')
#deals with request for second view
class SecondView(View):  
    def get(self, request) :
        u = reverse('gview:cats') #gets url from view function or objects
        u2 = reverse('gview:dogs')
        u3 = reverse('gview:dog', args=['42'] )
        ctx = {'x1' : u, 'x2': u2, 'x3': u3 }
        return render(request, 'route/second.html', ctx)

# References

# https://docs.djangoproject.com/en/3.0/topics/http/urls/#topics-http-reversing-url-namespaces


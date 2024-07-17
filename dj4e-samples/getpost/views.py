from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import html
from django.views.decorators.csrf import csrf_exempt
from django.views import View

# Call as dumpdata('GET', request.GET)

#utility function to dump data
#used in the functions below
#connects html form with django's library
def dumpdata(place, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

#get data from the form
def getform(request):
    response = """<p>Impossible GET guessing game...</p>
        <form>
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="submit"/>
        </form>"""

    response += dumpdata('GET', request.GET)
    return HttpResponse(response)

#Cross Site Request Forgery(CSRF) - a fake page stealing personal information with a similar form
#CSRF defense - a hidden field in the client(from db to maybe browers) with a token that is checked on the server
#free from CSRF check
@csrf_exempt
def postform(request):
    response = """<p>Impossible POST guessing game...</p>
        <form method="POST">
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="submit"/>
        </form>"""

    response += dumpdata('POST', request.POST)
    return HttpResponse(response)

#post for html4
@csrf_exempt
def html4(request):
    dump = dumpdata('POST', request.POST)
    return render(request, 'getpost/html4.html', {'data' : dump })

#post for html5
@csrf_exempt
def html5(request):
    dump = dumpdata('POST', request.POST)
    return render(request, 'getpost/html5.html', {'data' : dump })

#this view does not use a template with csrf token so it will fail
def failform(request):
    response = """<p>CSRF Fail guessing game...</p>
        <form method="post">
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="submit"/>
        </form>"""

    response += dumpdata('POST', request.POST)
    return HttpResponse(response)

from django.middleware.csrf import get_token

#csrf token added to the html form, so it will work
def csrfform(request):
    response = """<p>CSRF Success guessing game...</p>
        <form method="POST">
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="hidden" name="csrfmiddlewaretoken"
            value="__token__"/>
        <input type="submit"/>
        </form>"""

    token = get_token(request) #this can extract the token from the request
    response = response.replace('__token__', html.escape(token))
    response += dumpdata('POST', request.POST)
    return HttpResponse(response)

# Call as checkguess('42')
def checkguess(guess) :
    msg = False
    if guess :
        try:
            if int(guess) < 42 :
                msg = 'Guess too low'
            elif int(guess) > 42 :
                msg = 'Guess too high'
            else:
                msg = 'Congratulations!'
        except:
            msg = 'Bad format for guess:' + html.escape(guess)
    return msg

#view with URL Mapping with CSRF token
def guess(request):
    guess = request.POST.get('guess')
    msg = checkguess(guess)
    return render(request, 'getpost/guess.html', {'message' : msg })

#using class based views
class ClassyView(View) :
    def get(self, request):
        return render(request, 'getpost/guess.html')

    def post(self, request):
        guess = request.POST.get('guess')
        msg = checkguess(guess)
        return render(request, 'getpost/guess.html', {'message' : msg })

# Send a 302 and Location: header to the browser
def bounce(request) :
    return HttpResponseRedirect('https://www.dj4e.com/simple.htm')

#when a browser is refreshed, it will resend the last POST
#this is a problem if the POST was a purchase or a vote
#so the browser takes over and pops up a warning
#this is not good for the user experience
#so use a redirect after a post
#this class implements the redirect
class AwesomeView(View) :
    def get(self, request):
        msg = request.session.get('msg', False)
        if ( msg ) : del(request.session['msg'])
        return render(request, 'getpost/guess.html', {'message' : msg })

    def post(self, request):
        guess = request.POST.get('guess')
        msg = checkguess(guess)
        request.session['msg'] = msg
        return redirect(request.path) #redirects to the same page


# References

# https://stackoverflow.com/questions/3289860/how-can-i-embed-django-csrf-token-straight-into-html

# https://stackoverflow.com/questions/36347512/how-can-i-get-csrftoken-in-view

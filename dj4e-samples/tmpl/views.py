from django.shortcuts import render
from django.views import View

# Create your views here.

def simple(request):
    return render(request, 'tmpl/simple.html')
#applying template language
def guess(request) :
    context = {'zap' : '55' }
    return render(request, 'tmpl/guess.html', context)
#template with security and not. check the html
def special(request) :
    context = {'txt' : '<b>bold</b>',
               'zap' : '42' }
    return render(request, 'tmpl/special.html', context)
#loop logic is used with template language
def loop(request) :
    f = ['Apple', 'Orange', 'Banana', 'Lychee']
    n = ['peanut', 'cashew']
    x = {'fruits' : f, 'nuts' : n, 'zap' : '42' }
    return render(request, 'tmpl/loop.html', x)
#conditional logic
def cond(request) :
    x = {'guess' : '42' }
    return render(request, 'tmpl/cond.html', x)
#object oriented template language
def nested(request) :
    x = {'outer' : { 'inner' : '42' } }
    return render(request, 'tmpl/nested.html', x)
    
# Call this with a parameter number
#guess can be controlled by request
class GameView(View) :
    def get(self, request, guess) :
        x = {'guess' : int(guess) }
        return render(request, 'tmpl/cond.html', x)

# Using inheritance (extend)
#does the same as the original cond template 
class Game2View(View) :
    def get(self, request, guess) :
        x = {'guess' : int(guess) }
        return render(request, 'tmpl/cond2.html', x)


from django.http import HttpResponse

# Create your views here.

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', 
#     domain=None, secure=None, httponly=False, samesite=None)

#this function will check the cookies and set the cookies and expire date
#request can get the cookies since when Django gets the request, it will parse the cookies into a dictionary right away
def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is ' + str(oldval))
    if oldval : 
        resp.set_cookie('zap', int(oldval)+1) # No expired date = until browser close
    else : 
        resp.set_cookie('zap', 42) # No expired date = until browser close
    resp.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire
    return resp

# https://www.youtube.com/watch?v=Ye8mB6VsUHw

#this function will use session for each browser
#this will count the number of visits and store it in the database
def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits']) #python dictionary as session
    resp = HttpResponse('view count='+str(num_visits))
    return resp


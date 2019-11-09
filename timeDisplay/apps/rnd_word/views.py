from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
print('inside the views python file inside app->rnd_word')

def index(request):
    print('inside the index function of rnd_word app folder')
    return render( request,'rnd_word/homePgForGame.html')

def generateFun(request):
    print('inside the generate function')\
    
    rndW = get_random_string(length=10)
    # print(rndW)

    request.session['name'] = rndW
    print('the random word is', request.session['name'])

    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
        
    return redirect('/random_word')

def destroyFun(request):
    print('inside the destroy function')
    del request.session["count"]
    del request.session["name"]

    return redirect('/random_word')
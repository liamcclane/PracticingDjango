from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

def homePg(request):
    print('*-*-*-*-*-*-*-*inside homePf function*-*-*-*-*-')

    if 'amout_of_gold' in request.session:  # ie frist time around 
        request.session['amount_of_gold'] = 0    
    
    
    print('*-*-*-*-*-*-*-*end of homePf function*-*-*-*-*-')
    print('')
    return render(request,'dashboard/game.html')

def moneyProcess(request, methods = ['POST']):
    print('************inside moneyProcess function*****************')
    print("session.POST['key'] looks like : ", request.POST['key'])
    print("This is what post looks like with hidden inputs", request.POST)

    request.session['time'] = strftime("%Y-%m-%d  %H:%M %p", gmtime())

    # finding out which button they clicked to generate and add approiatley

    if 'farm' == request.POST['key']:
        diff = random.randint(10,20)
        print('\t inside the if statment of POST in farm')
        print('\t the random number between 10 and 20 is : ', diff)
    
    elif 'mine' == request.POST['key']:
        diff = random.randint(5,10)
        print('\t inside the if statment of POST in farm')
        print('\t the random number between 5 and 10 is : ', diff)
    
    elif 'home' == request.POST['key']:
        diff = random.randint(2,5)
        print('\t inside the if statment of POST in farm')
        print('\t the random number between 2 and 5 is : ', diff)
    
    else:
        # gamble' in request.session
        diff = random.randint(-50,50)
        print('\t inside the if statment of POST in gamble')
        print('\t the random number between -50 and 50 is : ', diff)

    # Now dealing with the output box
    if 'output' not in request.session:
        request.session['output'] = []  # initalize it
    
    if diff > 0:
        print('\t you are in the green and gained money')
        request.session['output'].insert(0,(f"Earned {diff} gold coins from the {request.POST['key']}! ({request.session['time']})",diff))
    
    elif diff < 0:
        request.session['output'].insert(0,(f"Lost {diff} gold coins from the {request.POST['key']}! ({request.session['time']})",diff))
        print('\t you suck and lost money')
    
    else:
        request.session['output'].insert(0,(f"Boke even with {diff} gold coins from the {request.POST['key']}! ({request.session['time']})",diff))
        print('\t broke even')


    request.session['amount_of_gold'] += diff
    print("the new amount should be : ", request.session['amount_of_gold'])
    print("the new out string should be : ", request.session['output'])

    print('************end function moneyProcess function************')
    print('')
    return redirect('/')

def reset(request):
    print('***---****---****---***inside the reset function***---***--***---***--***')
    request.session.clear()
    request.session['amount_of_gold'] = 0
    
    print('***---****---****---***end of the reset function***---***--***---***--***')
    print('')
    return redirect('/')
from django.shortcuts import render, redirect
from time import gmtime, strftime
    
def index(request):
    print('inside the index function inside the views file of singleApp folder')
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "name" : 'Nolle',
        "pets" : ["burce",'pets2', 'pets23'],
        'color' : "red"
    }
    print(context['time'])
    return render(request, "singleApp/index.html",  context)


def homePg(request):
    return render(request, 'singleApp/homePg.html')
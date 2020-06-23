from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'surname': 'Maheshwari'})
    # By using third parameter we are actually passing something from our view to out template, passed in Key Value
    # Pair and then on templates it will be referenced using Key
    # return HttpResponse("Hello Radhika")


def password(request):
    charcters = list('abcdefghijklmnopqrstuvwxyz')
    # Way to get the form data in our view, 12 is the default value in case user has not chosen length
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        charcters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('special'):
        charcters.extend('!@#$%^&*(){}|/*-+')

    if request.GET.get('numbers'):
        charcters.extend('1234567890')

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(charcters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request,"generator/about.html")

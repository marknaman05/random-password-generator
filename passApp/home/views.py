from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
#Random Password Generator
import random


def homepage(request):
    #return HttpResponse("<h2>This is a heading.</h2>")
    return render(request,'home/home.html')

def randomPass(request):
    s = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()"
    siz = request.GET.get('password') 
    print(siz)
    num = int(siz)
    password = "".join(random.sample(s,num))
    return HttpResponse('''<h2 style='background-color: rgb(209, 229, 247); font-family: 'Courier New', Courier, monospace;'>Your password of length {} is <i>{}</i></h2>'''.format(num,password))
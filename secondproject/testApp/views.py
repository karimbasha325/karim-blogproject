from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(request):
    date=datetime.datetime.now()
    s='<h1>Hello friends good morning..</h1> <hr>'
    s=s+'<h1>Time is '+str(date)+'</h1>'
    return HttpResponse(s)

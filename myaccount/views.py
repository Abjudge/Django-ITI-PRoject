from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Login(req):
    cont = {}
    cont["title"] = 'ITI REG'
    return render(req, 'index.html')

def reg (req):
    cont={}
    cont["title"]='ITI REG'
    return render(req ,'index.html')
def Logout (req):
    return HttpResponse("logout")
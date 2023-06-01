from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import *


def userlist(request):
    context={}
    context['users']=MyUser.objects.all()
    for u in MyUser.objects.all():
        print(u.id,u.username,u.password)
    return render(request,'listuser.html',context)
def Login(req):
    cont = {}
    if (req.method == 'POST'):
        u= MyUser.objects.filter(email=req.POST['lgemail'],password=req.POST['lgpassword'])
        if (len(u)!=0):
            req.session['username']=u[0].username
            return HttpResponseRedirect('/Course')
        else:
            cont['msg']= 'invalid user or password'
    return render(req, 'index.html', cont)

def reg (req):
    cont={}
    if (req.method =='POST'):
        username=req.POST['username']
        password = req.POST['password']
        email = req.POST['email']

        u=MyUser(username=username)

        u.password=password
        u.email=email
        u.actiiv=True
        u.save()
    return render(req ,'index.html',cont)
def Logout (req):
    req.session.clear()
    return HttpResponse("logout")
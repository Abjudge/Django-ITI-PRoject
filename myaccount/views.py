from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import *
from .form import *
from django.contrib.auth.models import *
from django.contrib.auth import login,authenticate
def userlist(request):
    context={}
    context['users']=MyUser.objects.all()
    for u in MyUser.objects.all():
        print(u.id,u.username,u.password)
    return render(request,'listuser.html',context)
def Login(req):
    cont = {}
    if (req.method == 'POST'):
        u= MyUser.objects.filter(username=req.POST['lgemail'],password=req.POST['lgpassword'])
        userobj=authenticate(username=req.POST['lgemail'],password=req.POST['lgpassword'] )
        if (len(u)!=0 and userobj is not None):
            req.session['username']=u[0].username
            login(req,userobj)
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

def RegAdmin (req):
    f = RegAdminForm()
    context = {}
    context['form'] = f
    if (req.method=="POST"):
        f = RegAdminForm(req.POST)
        if (f.is_bound and f.is_valid()):
            User.objects.create_superuser(username=req.POST['username'],password=req.POST['password'],email=req.POST['email'])
            return HttpResponseRedirect('/Admin')
    return render(req,"RegAdmin.html",context)

def RegAdminModel(req):
        f=RegAdminModelForm()
        context={}
        context['form']=f
        if (req.method=="POST"):
            f = RegAdminModelForm(req.POST)
            if (f.is_bound and f.is_valid()):
                f.save()
        return render(req,'RegAdminModel.html',context)
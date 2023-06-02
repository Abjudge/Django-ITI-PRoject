from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import *
from course import *
def traineelist(request):
    if( 'username' in request.session):
        trainees=Traineee.objects.all()
        context={}
        context["trainees"]=trainees
        return render(request,'trainee/list.html',context)
    else:
        return HttpResponseRedirect('/')

def traineeadd(request):

    if( 'username' in request.session):
        context= {}
        context['courses']=Course.objects.all()
        if (request.method=='POST'):
            cour=Course.objects.get(id=request.POST['coursename'])
            Traineee.objects.create(name=request.POST['traineename'],courseid=cour)

        return render(request,'trainee/add.html',context)
    else:
        return HttpResponseRedirect('/')

def traineeupdate(request,ID):

    context={}
    context['courses']=Course.objects.all()
    context['trainee'] = Traineee.objects.get(id=ID)
    if ('username' in request.session):
        if (request.method=="POST"):
            Traineee.objects.filter(id=ID).update(name=request.POST['traineename'],courseid=Course.objects.get(id=request.POST['coursename']) )
            return  HttpResponseRedirect("/Trainee")

        return render(request,'trainee/update.html',context)
    else:
        return HttpResponseRedirect('/')


def traineedelete(request, ID):
    Traineee.objects.filter(id=ID).delete()
    if ('username' in request.session):
        return HttpResponseRedirect('/Trainee')
    else:
        return HttpResponseRedirect('/')

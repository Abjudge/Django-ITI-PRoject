from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def traineelist(request):
    if( 'username' in request.session):
        return render(request,'trainee/list.html')
    else:
        return HttpResponseRedirect('/')

def traineeadd(request):

    if( 'username' in request.session):
        return render(request,'trainee/add.html')
    else:
        return HttpResponseRedirect('/')

def traineeupdate(request,id):

    if ('username' in request.session):
        return HttpResponse("Trainee " + str(id) + "updated")
    else:
        return HttpResponseRedirect('/')


def traineedelete(request, ID):

    if ('username' in request.session):
        return HttpResponse("Trainee "+str(ID)+"deleted")
    else:
        return HttpResponseRedirect('/')

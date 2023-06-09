from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from course import *
from rest_framework.status import   *
from django.shortcuts import  get_object_or_404
@api_view(['DELETE'])
def deletetrainee(request,id):

    if (Traineee.objects.filter(id=id).exists()):
        Traineee.objects.get(id=id).delete()
        return Response(status=HTTP_204_NO_CONTENT)



@api_view(['PUT'])
def updatetrainee(request,id):
    if (Traineee.objects.filter(id=id).exists()):
        trainee=Traineee.objects.get(id=id)
        serializer = TraineeSerializer(instance=trainee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_202_ACCEPTED,data= serializer.data)
        return Response(serializer.errors)
    else:
        return Response(status=HTTP_404_NOT_FOUND,data={"message":"trainee not found"})
@api_view(['POST'])
def addtrainee(request):
    serializer = TraineeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def alltrainee(request):
    trainees=Traineee.objects.all()
    if (trainees):
        serializer = TraineeSerializer(trainees, many=True)
        return Response(serializer.data)
    api_endpoints   = {
        "alltrainee":trainees
    }
    return Response(api_endpoints)

@api_view(['GET'])
def TraineeDetail(request,id):
    trainee=Traineee.objects.get(id=id)
    if (trainee):
        serializer = TraineeSerializer(trainee, many=False)
        return Response(serializer.data)
    api_endpoints   = {
        "alltrainee":trainee
    }
    return Response(  api_endpoints)



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

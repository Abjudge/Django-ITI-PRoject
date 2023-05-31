from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def traineelist(request):
    return HttpResponse("Traineelist")

def traineeadd(request):
    return HttpResponse("Traineeadd")
def traineeupdate(request,id):
    return HttpResponse("Trainee "+str (id)+"updated")


def traineedelete(request, ID):
    return HttpResponse("Trainee "+str(ID)+"deleted")

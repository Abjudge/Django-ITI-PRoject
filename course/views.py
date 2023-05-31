from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courselist(req):
    return render(req, 'home.html')

def courseadd(req):
    return render(req, 'home.html')
def courseupdate(request,id):
    return HttpResponse("course "+str (id)+"updated")


def coursedelete(request, ID):
    return HttpResponse("course "+str(ID)+"deleted")

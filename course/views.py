from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.views import View
class courselist(View):
    def get(self,request):
        return render(request, 'home.html')
    def post(self,request):
        pass
def courseadd(request):

    if ( 'username' in request.session):
        return render(request, 'course/add.html')
    else:
        return HttpResponseRedirect('/')
def courseupdate(request,id):
    if ( 'username' in request.session ):
        return HttpResponse("course " + str(id) + "updated")
    else:
        return HttpResponseRedirect('/')

def coursedelete(request, ID):


    if ( 'username' in request.session):
        return HttpResponse("course " + str(ID) + "deleted")
    else:
        return HttpResponseRedirect('/')

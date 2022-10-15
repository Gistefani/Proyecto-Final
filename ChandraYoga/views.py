from django.http import HttpResponse
from django.template import loader


def home(request):
    return HttpResponse('home')

def homePage(self):
       planilla = loader.get_template('home.html') 
       documento = planilla.render() 
       return HttpResponse(documento)

def homePage(self):
       planilla = loader.get_template('home.html') 
       documento = planilla.render() 
       return HttpResponse(documento)       
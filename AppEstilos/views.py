from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Estilo(request):
    return render (request,"Estilo.html") 
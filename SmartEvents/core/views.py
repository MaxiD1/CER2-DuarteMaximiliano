from django.shortcuts import render, HttpResponse
from .models import Contacto

def home(request):
    #return HttpResponse(titulo)
    return render(request,'core/home.html')
    
def events(request):
    #return HttpResponse(titulo)
    return render(request,'core/events.html')

def community(request):
    #return HttpResponse(titulo)
    return render(request,'core/community.html')
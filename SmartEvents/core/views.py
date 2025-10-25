from django.shortcuts import render, HttpResponse
from .models import evento


def home(request):
    #return HttpResponse(titulo)
    return render(request,'core/home.html')
    
def events(request):
    events = evento.objects.all().order_by('fecha')
    return render(request, 'core/events.html', {'eventos': events})

def community(request):
    #return HttpResponse(titulo)
    return render(request,'core/community.html')

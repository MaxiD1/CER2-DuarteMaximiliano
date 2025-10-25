from django.shortcuts import render, HttpResponse, redirect
from .models import evento
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    #return HttpResponse(titulo)
    return render(request,'core/home.html')
    
def events(request):
    events = evento.objects.all().order_by('fecha')
    return render(request, 'core/events.html', {'eventos': events})

def community(request):
    #return HttpResponse(titulo)
    return render(request,'core/community.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})
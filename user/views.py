from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your models here.
def RegisterView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)            
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'user/register.html', {'form':form})
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form':form})

def LoginView(request):
    if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password.")
            else: 
                messages.error(request, "Invalid username or password.")
                
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form})

def LogoutView(request):
    logout(request)
    return redirect('login')



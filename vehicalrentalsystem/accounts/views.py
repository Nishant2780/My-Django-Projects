from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


from django.contrib import messages
from .models import *
from django.urls import reverse
from .forms import *


# Create your views here.

def demo(request):
    return redirect("accounts:login_page")


def user_signup(request):
    if request.method == "POST":
        form_v = UserloginForm(request.POST, request.FILES)
        if form_v.is_valid():
            data = form_v.save()
            data.is_user = True
            data.set_password(data.password)
            data.save()
            return redirect("accounts:login_page")
        else:
            print(form_v.errors)
    else: 
        form_v = UserloginForm()
    return render (request, "accounts/user_signup.html", {'form': form_v})
        

def admin_signup(request):
    if request.method == "POST":
        form_v = adminloginForm(request.POST, request.FILES)
        if form_v.is_valid():
            data = form_v.save()
            data.is_super = True
            data.set_password(data.password)
            data.save()
            return redirect("accounts:login_page")
        else:
            print(form_v.errors)
    else: 
        form_v = adminloginForm()
    return render (request, "accounts/admin_signup.html", {'form': form_v})

    
def owner_signup(request):
    if request.method == "POST":
        form_v = ownerloginForm(request.POST, request.FILES)
        if form_v.is_valid():
            data = form_v.save()
            data.is_owner = True
            data.set_password(data.password)
            data.save()
            return redirect("accounts:login_page")
        else:
            print(form_v.errors)
    else: 
        form_v = ownerloginForm()
    return render (request, "accounts/owner_signup.html", {'form': form_v})

        
def login_page(request):        
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and user.is_super:
                login(request, user)
                return HttpResponseRedirect(reverse('admin_panel:home'))
            if user.is_active and user.is_user:
                login(request, user)
                return HttpResponseRedirect(reverse('user_panel:home'))
            if user.is_active and user.is_owner:
                login(request, user)
                return HttpResponseRedirect(reverse('owner_panel:home'))
            else:                
                messages.warning(request, 'User is Not Active')
                return HttpResponseRedirect(reverse('accounts:user_login'))
        else:
            print("error")
            messages.warning(request, 'Username or Password is Wrong')
            return HttpResponseRedirect(reverse('accounts:user_login'))
    else:
        return render(request, 'accounts/login.html', {})


def logout_user(request):
    logout(request)
    return redirect("accounts:login_page")





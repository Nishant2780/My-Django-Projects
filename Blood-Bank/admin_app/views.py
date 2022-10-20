from pyexpat import model
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout

from user_app.forms import UserloginForm
from django.views.generic import ListView, DetailView,CreateView
from user_app.models import AuthUser
# from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin

# Create your views here.


def demo(request):
    return redirect('admin_app:admin_signup')

def admin_home(request):
    return render(request, "admin_home.html")

class UserList(ListView):
    model = AuthUser
    template_name = "admin_app/user_list.html"
    context_object_name = "user_list"    

class UserDetails(DetailView):
    model = AuthUser
    template_name = "admin_app/user_details.html"
    context_object_name = "user"


# def details(request,id):
#     user = AuthUser.objects.get(id=id)
#     return render(request,'show.html', {'user':user})


def admin_signup(request):
    if request.method == "POST":
        form_v = UserloginForm(request.POST)
        if form_v.is_valid():
            asd = form_v.save()
            asd.is_admin = True
            asd.set_password(asd.password)
            asd.save()
            return redirect("admin_app:admin_signup")
        else:
            print(form_v.errors)
    else: 
        form_v = UserloginForm()
    return render (request, "admin_signup.html", {'form_v': form_v})


def admin_logout(request):
    logout(request)
    return redirect('user_app:login_user')

import time

def paras(request):
    while(True):
        print('dfgs')
        time.sleep(10)
    return render(request, "paras.html")

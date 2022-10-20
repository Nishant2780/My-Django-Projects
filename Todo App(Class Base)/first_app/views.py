
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView,UpdateView,DeleteView
from .models import Task   
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from .forms import *

# Create your views here.


def home(request):
    return redirect("first_app:userlogin")

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('first_app:ListTask') 
    else:
        form = UserForm()  
        return render (request, "login.html", {"form" : form})

def userlogout(request):
    logout(request)
    return redirect("first_app:userlogin")

class AddTask(CreateView):
    model = Task
    template_name = "AddTask.html"
    fields = ['Name', 'Description','Category']
    success_url = '/AddTask'

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            data = form.save(commit=False)
            data.User=request.user
            data.save()
        return redirect('first_app:ListTask')

class ListTask(ListView):
    model = Task
    template_name = "ListTask.html"
    context_object_name = "ListTask"

class UpdateTask(UpdateView):
    model = Task
    template_name = 'AddTask.html'
    fields = ['Name', 'Description', 'Category', 'Status']
    success_url ="/ListTask"

class DeleteTask(DeleteView):
    model = Task
    success_url = '/ListTask'

def Indoorfilters(request):
    Indoor = Task.objects.all().filter(Category = 'Indoor')
    return render(request, 'ListTask.html',{'ListTask': Indoor})
def Outdoorfilters(request):
    Outdoor = Task.objects.all().filter(Category = 'Outdoor')
    return render(request, 'ListTask.html',{'ListTask': Outdoor})
def createdatefilters(request):
    data = Task.objects.all().order_by('Create_date')
    return render(request, 'ListTask.html',{'ListTask': data})

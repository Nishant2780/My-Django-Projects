from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.urls import reverse
from .forms import *
from user_panel.models import *
import datetime


# Create your views here.

def home(request):
    return render(request, 'user_panel/home.html')

def Team(request):
    return render(request, "user_panel/Team.html")

def Available_Vehical(request):
    # data = Vehical_Registration.objects.all().exclude(UserId=request.user.id)
    types = VehicalType.objects.all()
    city = User.objects.all().values('State').distinct()
    data = Vehical_Registration.objects.filter(Status="Accepted").exclude(UserId=request.user.id)
    return render(request, 'user_panel/Available_Vehical.html', {'data' : data, 'types' : types, 'city' : city })


def type_wise_filter_in_userpanel(request,id):
    data = Vehical_Registration.objects.filter(Vahical_Type=id)
    types = VehicalType.objects.all()
    return render(request, 'user_panel/Available_Vehical.html', {'data' : data, 'types': types})

def City_filter_in_userpanel(request,state):
    
    types = VehicalType.objects.all()

    data = Vehical_Registration.objects.filter(UserId__State=state, Status="Accepted").exclude(UserId=request.user.id)
    print(data)
    return render(request, 'user_panel/Available_Vehical.html', {'data' : data, 'types': types})



def Rent_Request(request, id):
    
    r_vehicale=Vehical_Registration.objects.get(id=id)
    if request.method == 'POST':
        form = VehicalRequestForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.UserId=request.user
            data.VehicalId=r_vehicale
            delta = datetime.datetime.strptime(request.POST['EndDate'], "%Y-%m-%d") - datetime.datetime.strptime(request.POST['StartDate'], "%Y-%m-%d")
            data.Total_Price = delta.days * r_vehicale.Prize
            data.save()
            return HttpResponseRedirect(reverse('user_panel:home'))
        else:
            print(form.errors)
    else:
        form = VehicalRequestForm()
        abcd = VehicalRequest.objects.all()
    return render(request, 'user_panel/Rent_Request.html', {'form': form, 'data' : abcd, 'r_vehicale' : r_vehicale })



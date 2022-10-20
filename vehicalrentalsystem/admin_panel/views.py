from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.urls import reverse
from .forms import *
from user_panel.models import *

# from django.contrib.auth import authenticate, login, logout




# Create your views here.

def home(request):
    return render(request, 'admin_panel/home.html')

def create_type(request):
    if request.method == 'POST':
        form = VehicalTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_panel:create_type'))
        else:
            print(form.errors)
    else:
        form = VehicalTypeForm()
        data = VehicalType.objects.all()
    return render(request, 'admin_panel/vehical_type.html', {'form': form, 'data' : data})


def updatetype(request, id):
    details = VehicalType.objects.get(id=id)
    form_v = VehicalTypeForm(instance=details)
    if request.method == "POST":
        form_v = VehicalTypeForm(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:create_types")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/vehical_type.html", {'form' : form_v})


def deletetype(request, id):
  details = VehicalType.objects.get(id=id)
  details.delete()
  return redirect("admin_panel:create_type")





def addbrand(request):
    if request.method == 'POST':
        form = brandform(request.POST, request.FILES)
        if form.is_valid():
            
            data = form.save(commit=False)
            data.UserId=request.user
            data.save()
            return HttpResponseRedirect(reverse('admin_panel:addbrand'))
        else:
            print(form.errors)
    else:
        form = brandform()
        form = brandform()
        data = brand.objects.all()
    return render(request, 'admin_panel/vehical_brand.html', {'form': form,  'data' : data})



def updatebrand(request, id):
    details = brand.objects.get(id=id)
    form_v = brandform(instance=details)
    if request.method == "POST":
        form_v = brandform(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:addbrand")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/vehical_brand.html", {'form' : form_v})


def deletebrand(request, id):
  details = brand.objects.get(id=id)
  details.delete()
  return redirect("admin_panel:addbrand")



def category(request):
    if request.method == 'POST':
        form = category_listform(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.UserId=request.user
            data.save()
            return HttpResponseRedirect(reverse('admin_panel:category'))
        else:
            print(form.errors)
    else:
        form = category_listform()
        data = category_list.objects.all()
        types = VehicalType.objects.all()
    return render(request, 'admin_panel/vehical_category.html', {'form': form, 'data' : data, 'types': types})

def type_wise_category(request, id):
    
    form = category_listform()
    data = category_list.objects.filter(Vehical_TypeID=id)
    types = VehicalType.objects.all()
    return render(request, 'admin_panel/vehical_category.html', {'form': form, 'data' : data, 'types': types})
    


def updatecategory(request, id):
    details = category_list.objects.get(id=id)
    form_v = category_listform(instance=details)
    if request.method == "POST":
        form_v = category_listform(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:category")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/vehical_category.html", {'form' : form_v})


def deletecategory(request, id):
    details = category_list.objects.get(id=id)
    details.delete()
    return redirect("admin_panel:category")





def Add_Vehical_Variant(request):
    if request.method == 'POST':
        form = vehical_Variantform(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.UserId=request.user
            data.save()
            return HttpResponseRedirect(reverse('admin_panel:Vehical_Variant'))
        else:
            print(form.errors)
    else:
        form = vehical_Variantform()
        data = vehical_Variant.objects.all()        
    return render(request, 'admin_panel/Add_Variant.html', {'form': form, 'data' : data})

def type_wise_category_in_variant(request, id):

    form = vehical_Variantform()
    data = vehical_Variant.objects.filter(Vahical_Type=id)
    types = VehicalType.objects.all()
    return render(request, 'admin_panel/Vehical_Variant.html', {'form': form, 'data' : data, 'types': types})



def Vehical_Variant(request):
    form = vehical_Variantform()
    types = VehicalType.objects.all()
    data = vehical_Variant.objects.all()
    return render(request, 'admin_panel/Vehical_Variant.html', { 'data' : data, 'types': types, 'form': form })
    

def updatevariant(request, id):
    details = vehical_Variant.objects.get(id=id)
    form_v = vehical_Variantform(instance=details)
    if request.method == "POST":
        form_v = vehical_Variantform(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:Vehical_Variant")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/Add_Variant.html", {'form' : form_v})


def deletevariant(request, id):
    details = vehical_Variant.objects.get(id=id)
    details.delete()
    return redirect("admin_panel:Vehical_Variant")


def vehical_Registration(request):
    if request.method == 'POST':
        form = Vehical_Registrationform(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.UserId=request.user
            data.Status = "Accepted"
            data.save()
            return HttpResponseRedirect(reverse('admin_panel:Register_Vehical_List'))
        else:
            print(form.errors)
    else:
        form = Vehical_Registrationform()
        data = Vehical_Registration.objects.all()
    return render(request, 'admin_panel/Vehical_Registration.html', {'form': form, 'data' : data})

def type_wise_filter_in_registration(request,id):

    form = Vehical_Registrationform()
    types = VehicalType.objects.all()
    data = Vehical_Registration.objects.filter(Vahical_Type=id)
    return render(request, 'admin_panel/Register_Vehical_List.html', {'form': form, 'data' : data, 'types' : types})


def Register_Vehical_List(request):
    types = VehicalType.objects.all()
    data = Vehical_Registration.objects.all()
    return render(request, 'admin_panel/Register_Vehical_List.html', {'data' : data, 'types': types})


def update_Register_Vehical(request, id):
    details = Vehical_Registration.objects.get(id=id)
    form_v = Vehical_Registrationform(instance=details)
    if request.method == "POST":
        form_v = Vehical_Registrationform(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:Register_Vehical_List")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/Vehical_Registration.html", {'form' : form_v})


def delete_Register_Vehical(request, id):
    details = Vehical_Registration.objects.get(id=id)
    details.delete()
    return redirect("admin_panel:Register_Vehical_List")





def Users(request):
    data = User.objects.all()
    return render(request, 'admin_panel/user_details.html', {'data' : data})

def deleteUsers(request, id):
    details = User.objects.get(id=id)
    details.delete()
    return redirect("admin_panel:Users")


def owner_rq_List(request):
    data = Vehical_Registration.objects.all().exclude(UserId=request.user.id)
    # data = Vehical_Registration.objects.filter(UserId=request.user.id, Status="Available")
    return render(request, 'admin_panel/owner_Rq_List.html', {'data' : data})

def accept_owner_req(request, id):
    data = Vehical_Registration.objects.get(id=id)
    data.Status = "Accepted"
    data.save()
    return redirect("admin_panel:owner_rq_List")

def reject_owner_req(request, id):
    data = Vehical_Registration.objects.get(id=id)
    data.Status = "Rejected"
    data.save()
    return redirect("admin_panel:owner_rq_List")
    



def Rent_Rq_List_admin(request):
    data = VehicalRequest.objects.all()
    # data = VehicalRequest.objects.filter(VehicalId__UserId=request.user.id)
    # data = Vehical_Registration.objects.filter(UserId=request.user.id, Status="Available")
    return render(request, 'admin_panel/Rent_Rq_List_admin.html', {'data' : data})

def accept_rent_req(request, id):
    data = VehicalRequest.objects.get(id=id)
    data.Status = "Accepted"
    data.save()
    return redirect("admin_panel:Rent_Rq_List_admin")

def reject_rent_req(request, id):
    data = VehicalRequest.objects.get(id=id)
    data.Status = "Rejected"
    data.save()
    return redirect("admin_panel:Rent_Rq_List_admin")





def Available_Vehical_List(request):
    # data = Vehical_Registration.objects.all().exclude(UserId=request.user.id)
    data = Vehical_Registration.objects.filter(Status="Accepted")
    types = VehicalType.objects.all()
    return render(request, 'admin_panel/Available_Vehical_List.html', {'data' : data, 'types' : types})

def type_wise_filter_in_Available_Vehical(request,id):
    data = Vehical_Registration.objects.filter(Vahical_Type=id)
    types = VehicalType.objects.all()
    return render(request, 'admin_panel/Available_Vehical_List.html', {'data' : data, 'types': types})
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from admin_panel.models import *
from admin_panel.forms import *
from manager_panel.models import *
from manager_panel.forms import *

# Create your views here.

def home(request):
    return render(request, 'admin_panel/home.html')

def add_product_type(request):
    if request.method == 'POST':
        form = ProductsTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_panel:home'))
        else:
            print(form.errors)
    else:
        form = ProductsTypeForm()
    return render(request, 'admin_panel/add_product_type.html', {'form': form})


def product_type_list(request):
    types = ProductType.objects.all()
    return render(request, 'admin_panel/product_type_list.html', {'types': types})

def update(request, id):
    details = ProductType.objects.get(id=id)
    form_v = ProductsTypeForm(instance=details)
    if request.method == "POST":
        form_v = ProductsTypeForm(request.POST, request.FILES,  instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:product_type_list")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/add_product_type.html", {'form' : form_v})

def delete(request, id):
  details = ProductType.objects.get(id=id)
  details.delete()
  return redirect("admin_panel:product_type_list")

def add_Products_Details(request):
    if request.method == 'POST':
        form = Products_Details_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_panel:home'))
        else:
            print(form.errors)
    else:
        form = Products_Details_Form()
    return render(request, 'admin_panel/products_details_form.html', {'form': form})

def List_Products_Details(request):
    
    types = Products_Details.objects.all()
    return render(request, 'admin_panel/products_details.html', {'types': types})


def Requestupdate(request, id):
    details = Products_Details.objects.get(id=id)
    form_v = Products_Details_Form(instance=details)
    if request.method == "POST":
        form_v = Products_Details_Form(request.POST, request.FILES, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:List_Products_Details")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/products_details_form.html", {'form' : form_v})

def Requestdelete(request, id):
  details = Products_Details.objects.get(id=id)
  details.delete()
  return redirect("admin_panel:List_Products_Details")

def add_company(request):
    if request.method == 'POST':
        form = Comapany_Details_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_panel:home'))
        else:
            print(form.errors)
    else:
        form = Comapany_Details_Form()
    return render(request, 'admin_panel/add_company.html', {'form': form})


def company_list(request):
    types = Comapany_Details.objects.all()
    return render(request, 'admin_panel/company_list.html', {'types': types})


def Requpdate(request, id):
    details = Comapany_Details.objects.get(id=id)
    form_v = Comapany_Details_Form(instance=details)
    if request.method == "POST":
        form_v = Comapany_Details_Form(request.POST, request.FILES, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:company_list")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/add_company.html", {'form' : form_v})

def Reqdelete(request, id):
  details = Comapany_Details.objects.get(id=id)
  details.delete()
  return redirect("admin_panel:company_list")


def add_suppliers(request):
    if request.method == 'POST':
        form = suppliers_Form(request.POST, request.FILES)
        if form.is_valid():
            
            data = form.save(commit=False)
            print(request.user)
            data.User_id = request.user
            data.save()
            return HttpResponseRedirect(reverse('admin_panel:home'))
        else:
            print(form.errors)
    else:
        form = suppliers_Form()
    return render(request, 'admin_panel/add_suppliers.html', {'form': form})


def suppliers_list(request):
    types = suppliers.objects.all()
    return render(request, 'admin_panel/suppliers_list.html', {'types': types})

def suppliers_update(request, id):
    details = suppliers.objects.get(id=id)
    form_v = suppliers_Form(instance=details)
    if request.method == "POST":
        form_v = suppliers_Form(request.POST, request.FILES,  instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:suppliers_list")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/add_suppliers.html", {'form' : form_v})

def suppliers_delete(request, id):
  details = suppliers.objects.get(id=id)
  details.delete()
  return redirect("admin_panel:suppliers_list")


from django.views.generic.detail import DetailView
from django_xhtml2pdf.views import PdfMixin


class ProductPdfView(PdfMixin, DetailView):
    model = Products_Details
    template_name = "admin_panel/product_pdf.html"


def quotations_list_admin(request):
    types = quotations.objects.all()
    return render(request, 'admin_panel/quotations_list.html', {'types': types})

def accept_quo_req(request, id):
    data = quotations.objects.get(id=id)
    data.Status = "Accepted"
    data.save()
    return redirect("admin_panel:quotations_list_admin")

def reject_quo_req(request, id):
    data = quotations.objects.get(id=id)
    data.Status = "Rejected"
    data.save()
    return redirect("admin_panel:quotations_list_admin")
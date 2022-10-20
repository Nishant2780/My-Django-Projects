from django.urls import path
from django import views
from first_app import views

app_name = 'first_app'

urlpatterns = [
    
    path('', views.home, name='home'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),

    path('AddTask/', views.AddTask.as_view(), name = 'AddTask'),
    path('ListTask/', views.ListTask.as_view(), name = 'ListTask'),
    path('update/<pk>', views.UpdateTask.as_view(), name = 'update'),
    path('delete/<pk>', views.DeleteTask.as_view(), name = 'delete'),

    path('OutdoorTask/', views.Outdoorfilters, name = 'Outdoorfilters'),
    path('IndoorTask/', views.Indoorfilters, name = 'Indoorfilters'),
    path('datewisefilter/', views.createdatefilters, name = 'createdatefilters'),

]

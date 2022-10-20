from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "owner_panel"

urlpatterns = [
    
    path('home/', views.home, name='home'),

    path('Rent_Vehical/', views.Rent_Vehical, name='Rent_Vehical'),
    
    path('ownervehicledetails/', views.ownervehicledetails, name='ownervehicledetails'),
    path('delete_vehicle/<int:id>', views.delete_vehicle, name='delete_vehicle'),




   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
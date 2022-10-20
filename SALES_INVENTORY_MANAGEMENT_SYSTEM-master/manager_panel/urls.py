from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "manager_panel"

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product_type/', views.add_product_type, name='add_product_type'),
    path('product_type_list', views.product_type_list, name='product_type_list'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
    path('List_Products_Details/', views.List_Products_Details, name="List_Products_Details"),
    path('add_Products_Details/', views.add_Products_Details, name="add_Products_Details"),
    path('Requestupdate/<int:id>/', views.Requestupdate, name="Requestupdate"),
    path('Requestdelete/<int:id>', views.Requestdelete, name="Requestdelete"),
    path('add_company/', views.add_company, name="add_company"),
    path('company_list/', views.company_list, name="company_list"),
    path('Requpdate/<int:id>/', views.Requpdate, name="Requpdate"),
    path('Reqdelete/<int:id>', views.Reqdelete, name="Reqdelete"),

    path('product_pdf/<int:pk>', views.ProductPdfView.as_view(), name="product_pdf"),
    
    path('add_quotations_type/', views.add_quotations_type, name="add_quotations_type"),
    path('quotations_list/', views.quotations_list, name="quotations_list"),
    

]

   
from unicodedata import name
from django.urls import path
from admin_app import views

app_name = "admin_app"

urlpatterns = [
    
    path('', views.demo, name='demo'),
    path('admin_home/', views.admin_home, name='admin_home'),

    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

    path('user_list/', views.UserList.as_view(), name="user_list"),
    path('user_list/<int:pk>', views.UserDetails.as_view(), name="user_details"),
    path('paras/', views.paras, name="paras"),

]
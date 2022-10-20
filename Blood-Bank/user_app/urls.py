from django.urls import path
from user_app import views

app_name = "user_app"

urlpatterns = [
    
    path('', views.demo, name='demo'),
    path('user_home/', views.user_home, name='user_home'),
    
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('demo_submit/', views.images_submit, name='images_submit'),

    path('add_user/', views.add_user, name='add_user'),



]
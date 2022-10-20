from enroll import views
from django.urls import path

app_name = "enroll"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('save/', views.save_data, name = 'save'),
    path('edit/', views.edit_data, name = 'edit'),
    path('delete/', views.delete_data, name = 'delete'),
]
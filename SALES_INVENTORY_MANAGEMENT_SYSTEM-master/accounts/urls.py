from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "accounts"

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('Accountant_signup/', views.Accountant_signup, name='Accountant_signup'),
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('manager_signup/', views.manager_signup, name='manager_signup'),

    path('logout_user/', views.logout_user, name='logout_user'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


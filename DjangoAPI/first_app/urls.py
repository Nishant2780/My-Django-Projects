from django.urls import path
from . import views
from .views import *

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename='todo-view-set')   #--- view set url 


urlpatterns = [
    path('', views.home, name="home"),
    path('get-todo/', views.get_todo, name = 'get-todo'),
    path('post-todo/', views.post_todo, name = 'post-todo'),
    path('patch-todo/', views.patch_todo, name = 'patch-todo'),

    path('todo/', views.TodoView.as_view(), name = 'todoview'),

    # path('prduct_type_api', views.prduct_type_api, name="prduct_type_api"),
    # path('products_details_api', views. products_details_api, name="products_details_api"),
]

urlpatterns += router.urls
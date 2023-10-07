from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('panel/', views.panel, name='panel'),
    path('login/', views.mylogin, name='mylogin'),
    path('logout/', views.mylogout, name='mylogout'),
    path('panel/setting/', views.site_setting, name='site_setting'),
   
]

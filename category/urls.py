from django.urls import path, include
from . import views


# app_name = 'category'

urlpatterns = [
    path('panel/category/list/', views.category_list, name='category_list' ),
    path('panel/category/add/', views.category_add, name='category_add' ),  

]
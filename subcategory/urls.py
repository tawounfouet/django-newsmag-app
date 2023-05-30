from django.urls import path, include
from . import views


# app_name = 'category'

urlpatterns = [
    path('panel/subcategory/list/', views.subcategory_list, name='subcategory_list' ),
    path('panel/subcategory/add/', views.subcategory_add, name='subcategory_add' ),  

]
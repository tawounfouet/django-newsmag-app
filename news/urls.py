from django.urls import path, include
from . import views


# app_name = 'news'

urlpatterns = [
    #path('news/<str:title>/', views.news_detail, name='news_detail' ), 
    # path('news/(?P<word>.*)/$', views.news_detail, name='news_detail' ),   
    path('news/<str:pk>/', views.news_detail, name='news_detail' ), 
    path('panel/news/list/', views.news_list, name='news_list' ),
    path('panel/news/add/', views.news_add, name='news_add'),
    path('panel/news/edit/<str:pk>/', views.news_edit, name='news_edit'),
    path('panel/news/delete/<str:pk>/', views.news_delete, name='news_delete'),
    
]
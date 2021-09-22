from django.contrib import admin
from django.urls import path
from . import views



app_name='telas'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path("new-user", views.new_user_ajax, name='new_user_ajax'),
    #path('novo-usuario', views.new_user, name='new-user'),

]

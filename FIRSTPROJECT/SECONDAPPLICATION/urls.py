from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('R/', views.home,name="Register"),
    path('',views.emp,name="emp_register"),
    path('show',views.show,name="show")
    
    
]

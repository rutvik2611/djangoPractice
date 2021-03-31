from django.contrib import admin
from django.urls import path,include
from FIRSTAPPLICATION import views
urlpatterns = [
    
    path('',views.not_home),
    path('r/',views.home)
    
]

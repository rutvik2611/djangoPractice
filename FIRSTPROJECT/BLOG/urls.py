from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('blog/',views.signup),
    path('blog/welcome/',views.Welcome)
]

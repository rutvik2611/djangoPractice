from django.contrib import admin
from django.urls import path,include
from FIRSTAPPLICATION import views,forms
urlpatterns = [
    
    path('',views.not_home),
    path('r/',views.home),
    path('signup/',views.signup),
    path('register/',views.signup2)
    
    
]

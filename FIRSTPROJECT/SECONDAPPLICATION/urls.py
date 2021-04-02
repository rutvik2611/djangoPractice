from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('R/', views.home,name="Register"),
    path('',views.emp,name="emp_register"),
    path('show',views.show,name="show"),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    
    
]

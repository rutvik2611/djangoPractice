from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('blog/',views.signup),
    # path('blog/welcome/',views.Welcome),
    path('blog/login/',views.login),
    path('blog/show',views.Show),
    path('blog/delete/<int:id>',views.delete_registration),
    path('blog/edit/<int:id>',views.edit_registration),
    path('blog/update/<int:id>',views.update_registration)
]

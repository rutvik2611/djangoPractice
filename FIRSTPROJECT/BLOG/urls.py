from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers


router=routers.DefaultRouter()
urlpatterns = [
    
    path('blog/',views.signup),
    # path('blog/welcome/',views.Welcome),
    path('blog/login/',views.login),
    path('blog/show',views.Show),
    path('blog/delete/<int:id>',views.delete_registration),
    path('blog/edit/<int:id>',views.edit_registration),
    path('blog/update/<int:id>',views.update_registration),
    path('blog/login2/',views.login2),
    path('blog/json',views.random),
    path('blog/api',views.RegList.as_view()),
    path('blog/login/create',views.blog_form_view),
    path('blog/login/create/show',views.show_blog),
    path('blog/login/blog/x/<int:id>',views.blog_delet),
    
]

"""
URL configuration for travels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [

    path('index/',views.index),
    path('tours/',views.tours),
    path('destinations/',views.destinations),
    path('news/',views.news),
    path('contact/',views.contact),
    path('about/',views.about),
    path('login/',views.login),
    path('register/',views.register),
    path('formcode/',views.formcode),
    path('contact/',views.contact),
    path('signupcode/',views.signupcode),
    path('admins/',views.admin),
    path('log/',views.log),
    path('cont/',views.cont),
    path('reg/',views.reg),
    #path('admin_login/',views.admin_login),
    path('delete/<int:id>',views.delete),
    path('deletedata/<int:id>',views.deletedata),
    path('edit/<int:id>',views.edit),
    path('update/',views.update),
    path('editdata/<int:id>',views.editdata),
    path('updatecode/',views.updatecode),
    # path('login/',views.login),
    path('adminlogin/',views.adminlogin),
    path('logincode/',views.logincode),
    path('logcode/',views.logcode),


]

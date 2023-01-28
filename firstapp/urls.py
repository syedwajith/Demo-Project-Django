"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from firstapp import views

urlpatterns = [
    path('reg/',views.registerpage),
    path('userlog/',views.userlogin,),
    path('adminlog/',views.adminlogin,),
    path('pending/',views.pending,),
    path('approved/',views.approved,),
    path('approve/<int:id>/',views.approve),
    path('edit/<int:id>/',views.edit),
    path('delete/<int:id>/',views.delete),
]
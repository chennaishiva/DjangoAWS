"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from FirstWebApp import views as v1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.Homepage),
    path('register/', v1.Register),
    path('login/', v1.Login),
    path('second/', include("SecondWebApp.urls")),
    path('forms/', include("FormsWebApp.urls")),
    path('curd/', include("curdapp.urls")),
    path('alert/', include("AlertApp.urls")), #http://127.0.0.1:8000/alert/..
    path('rest/', include("RestAPI.urls")), #http://127.0.0.1:8000/rest/..
]

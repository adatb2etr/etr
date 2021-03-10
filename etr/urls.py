"""etr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from register import views as v
from user.views import *
from terem.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("registeradmin/", v.register, name="register"),
    path("register/", v.registerFelhasznalo, name="registerFelhasznalo"),
    path("teszt/", v.sample_view, name="teszt"),
    path('', include("django.contrib.auth.urls")),  #login
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),


    path('felhasznalok/', felhasznalok_list_view, name="FelhasznalokList"),    #oktatok_list_view függvényt használja
    path('felhasznalok/<str:UserAzonosito>/', felhasznalok_lookup_view, name="FelhasznaloView"),   #OktatokView  -  models.py-ban lévő reverse függénynél használjuk, ezzel kapjuk meg az oktato_azonosítót és ezzel hívja meg a oktato_lookup_view -t.
    path('felhasznalok/<str:UserAzonosito>/update/',felhasznalok_update_view, name="FelhasznaloUpdateView"),
    path('felhasznalok/<str:UserAzonosito>/delete/', felhasznalok_delete_view, name="FelhasznaloDeleteView"),
    path('me/', sajat_detail_view, name="Me"),

    path('termek/create/', terem_create_view, name ='terem-create'),
    path('termek/<str:terem_cim>/', terem_lookup_view, name='terem-detail'),
    path('termek/<str:terem_cim>/update/', terem_update_view, name='terem-update'),
    path('termek/<str:terem_cim>/delete/', terem_delete_view, name='terem-delete'),
    path('termek/', terem_list_view, name='Terem lista'),
]

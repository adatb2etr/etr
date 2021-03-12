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
from kurzus.views import *
from idopont.views import *

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

    path('kurzusok/create/', kurzus_create_view, name ='kurzus-create'),
    path('kurzusok/<str:kurzus_kod>/', kurzus_lookup_view, name='kurzus-detail'),
    path('kurzusok/<str:kurzus_kod>/update/', kurzus_update_view, name='kurzus-update'),
    path('kurzusok/<str:kurzus_kod>/delete/', kurzus_delete_view, name='kurzus-delete'),
    path('kurzusok/', kurzus_list_view, name='Kurzus lista'),

    path('idopontok/create/', idopont_create_view, name='idopont-create'),
    path('idopontok/<int:idopont_id>/', idopont_lookup_view, name='idopont-detail'),
    path('idopontok/<int:idopont_id>/update/', idopont_update_view, name='idopont-update'),
    path('idopontok/<int:idopont_id>/delete/', idopont_delete_view, name='idopont-delete'),
    path('idopontok/', idopont_list_view, name='Idopont lista'),
]

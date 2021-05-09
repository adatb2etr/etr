from django.shortcuts import render
from user.forms import EtrAdminForm, FelhasznaloForm, FelhasznaloLoginForm
from user.models import EtrAdmin, Oktato, Hallgato
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import hashlib
from django.contrib.auth.hashers import make_password
from user.validators.validators import is_EtrAdmin, is_Oktato, is_Hallgato
from user.validators.queries import getids
from django.shortcuts import redirect
from user.validators.queries import getRole
from tartozas.admin import Tartozas
from osztondij.models import Osztondij
import random, string
from django.contrib.auth.forms import UserCreationForm

# /registeradmin/
def register(response):
    if True:#is_EtrAdmin(response) is True:    
        if response.method == "POST":
            form = EtrAdminForm(response.POST)
            if form.is_valid():
                #A 2 JELSZÓ MEZŐT ÖSSZEHASONLíTJA, ÉS HA MEGEGYEZIK AKKOR KREÁLJA AZ ACCOUNTOT
                if form.data['jelszo'] == form.data['jelszo2']:
                    #KREÁL EGY USER OBJECTET A DJANGO USER TÁBLÁJÁNAK IS, HOGY BE LEHESSEN LÉPNI AZ OLDALRA

                    encryptedJelszo = (hashlib.sha256(form.data['jelszo'].encode())).hexdigest()  #sima sha256 encryption.
                    userJelszo = make_password(form.data['jelszo'])   # ez a django password encryptiont használja, dont tuch, ez a django_user táblához kell

                    User.objects.create(username=form.data['azonosito'], first_name=form.data['keresztnev'],
                                        last_name=form.data['vezeteknev']
                                        , email=form.data['email'], password=userJelszo)

                    print(f"\n\n\n\n{form.data['jelszo']}\n\n\n\n")
                    EtrAdmin.objects.create(azonosito=form.data['azonosito'], keresztnev=form.data['keresztnev'], vezeteknev=form.data['vezeteknev']
                                        ,email=form.data['email'], jelszo=encryptedJelszo, telefonszam=form.data['telefonszam'])
                else:
                    print(f"\n\n\n\nRossz a 2 jelszó!\n\n\n\n")
        else:
            form = EtrAdminForm()
    return render(response, "register/registerAdmin.html", {"form": form})



# /register/
def registerFelhasznalo(response):
    if is_EtrAdmin(response) is True:
        if response.method == "POST":
            form = FelhasznaloForm(response.POST)
            if form.is_valid():
                if form.data['jelszo'] == form.data['jelszo2']:

                    encryptedJelszo = (hashlib.sha256(form.data['jelszo'].encode())).hexdigest()  #sima sha256 encryption.
                    userJelszo = make_password(form.data['jelszo'])

                    if form.data['account_type'] == "2":
                        print(f"oktato")
                        oktato = True
                    else:
                        print(f"oktato nem")
                        oktato = False

                    if form.data['account_type'] == "1":
                        print(f"hallgato")
                        hallgato = True
                    else:
                        print(f"hallgato nem")
                        hallgato = False

                    if oktato is True and hallgato is False:
                        id = "TESZTADMIN"
                        foglaltIDs = getids()

                        while id in foglaltIDs or id == "TESZTADMIN":
                            chars = string.ascii_uppercase + string.digits
                            id = "".join(random.choice(chars) for i in range(6))

                        User.objects.create(username=id, first_name=form.data['keresztnev'],
                                            last_name=form.data['vezeteknev']
                                            , email=form.data['email'], password=userJelszo)

                        print(f"\n\n\n\n{form.data['jelszo']}\n\n\n\n")
                        Oktato.objects.create(azonosito=id, keresztnev=form.data['keresztnev'], vezeteknev=form.data['vezeteknev']
                                            ,email=form.data['email'], jelszo=encryptedJelszo, telefonszam=form.data['telefonszam'], szulido=form.data['szulido'],
                                                szemelyiszam=form.data['szemelyiszam'])

                        print(f"\n\n\nAz oktató ID-ja: {id}\n\n\n")


                    elif hallgato is True and oktato is False:
                        print(f"hallgato")
                        id = "TESZTADMIN"
                        foglaltIDs=getids()

                        while id in foglaltIDs or id == "TESZTADMIN":
                            chars = string.ascii_uppercase + string.digits
                            id = "".join(random.choice(chars) for i in range(6))


                        User.objects.create(username=id, first_name=form.data['keresztnev'],
                                            last_name=form.data['vezeteknev']
                                            , email=form.data['email'], password=userJelszo)

                        print(f"\n\n\n\n{form.data['jelszo']}\n\n\n\n")
                        Hallgato.objects.create(azonosito=id, keresztnev=form.data['keresztnev'],
                                              vezeteknev=form.data['vezeteknev']
                                              , email=form.data['email'], jelszo=encryptedJelszo,
                                              telefonszam=form.data['telefonszam'], szulido=form.data['szulido'],
                                              szemelyiszam=form.data['szemelyiszam'])

                        print(f"\n\n\nA hallgató ID-ja: {id}\n\n\n")


                else:
                    print(f"\n\n\n\nHiba!\n\n\n\n")

        else:
            form = FelhasznaloForm()
        return render(response, "register/registerFelhasznalo.html", {"form": form})
    else:
        return redirect("../")

# /
def loginPage(request):
    if is_Hallgato(request) or is_Oktato(request) or is_EtrAdmin(request):
        return redirect("/me")
    else:
        form = FelhasznaloLoginForm(request.POST or None)
        if form.is_valid():
            username = form.data["neptunkod"]
            password = form.data["jelszo"]
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                print("loginPage redirect to /me")
                return redirect("/me")
            else:
                request.session['invalid_user'] = 1
        context = {'form': form}
        return render(request, 'registration/login.html', context)

# /logout
def logoutPage(request):
    logout(request)
    return redirect("/")

def sample_view(response):
    print("gomb megnyomva")
    return render(response, "teszt.html")
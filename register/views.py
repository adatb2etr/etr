from django.shortcuts import render
from user.forms import EtrAdminForm, FelhasznaloForm
from user.models import EtrAdmin, Oktato, Hallgato
from django.contrib.auth.models import User
import hashlib
from django.contrib.auth.hashers import make_password
from user.validators.validators import is_EtrAdmin, is_Oktato, is_Hallgato
from user.validators.queries import getids
from django.shortcuts import redirect
import random, string

# /registeradmin/
def register(response):
    if is_EtrAdmin(response) is True:
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
    else:
        return render(response, "teszt.html")


# /register/
def registerFelhasznalo(response):
    if is_EtrAdmin(response) is True:
        if response.method == "POST":
            form = FelhasznaloForm(response.POST)
            if form.is_valid():
                if form.data['jelszo'] == form.data['jelszo2']:

                    encryptedJelszo = (hashlib.sha256(form.data['jelszo'].encode())).hexdigest()  #sima sha256 encryption.
                    userJelszo = make_password(form.data['jelszo'])

                    if 'Oktato' in response.POST:
                        oktato = True
                    else:
                        oktato = False

                    if 'Hallgato' in response.POST:
                        hallgato = True
                    else:
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
        return redirect("../teszt/")


from elofeltetel.models import Elofeltetel
from kurzustfelvesz.models import Kurzustfelvesz

def sample_view(response):

    print("gomb megnyomva")
    return render(response, "teszt.html")

from etr.wsgi import *
from user.models import EtrAdmin, Oktato, Hallgato

def getids():
    ids = []
    etradminok = EtrAdmin.objects.values_list('azonosito', flat=True)
    oktatok = Oktato.objects.values_list('azonosito', flat=True)
    hallgatok = Hallgato.objects.values_list('azonosito', flat=True)

    for id in etradminok:
        ids.append(id)

    for id in oktatok:
        ids.append(id)

    for id in hallgatok:
        ids.append(id)

    return ids

def getEtrAdminIds():

    ids = []
    etradminok = EtrAdmin.objects.values_list('azonosito', flat=True)


    for id in etradminok:
        ids.append(id)

    return ids


def getOktatoIds():
    ids = []
    oktatok = Oktato.objects.values_list('azonosito', flat=True)

    for id in oktatok:
        ids.append(id)

    return ids


def getHallgatoIds():
    ids = []
    hallgatok = Hallgato.objects.values_list('azonosito', flat=True)

    for id in hallgatok:
        ids.append(id)

    return ids


def getRole(id):

    try:
        EtrAdmin.objects.get(azonosito=id)
        return "admin"
    except:
        try:
            Oktato.objects.get(azonosito=id)
            return "oktato"
        except:
            try:
                Hallgato.objects.get(azonosito=id)
                return "hallgato"
            except:
                return None



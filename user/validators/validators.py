from user.models import EtrAdmin, Oktato, Hallgato

def is_EtrAdmin(response):

    admin = EtrAdmin.objects.all().filter(azonosito=response.user)
    if admin:
        return True
    else:
        return False

def is_Oktato(response):

    oktato = Oktato.objects.all().filter(azonosito=response.user)
    if oktato:
        return True
    else:
        return False

def is_Hallgato(response):

    hallgato = Hallgato.objects.all().filter(azonosito=response.user)
    if hallgato:
        return True
    else:
        return False

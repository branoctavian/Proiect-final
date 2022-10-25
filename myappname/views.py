from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from marketplace.produse.functii import listeaza_toate_produsele
from marketplace.comenzi.functii import listeaza_toate_comenzile
from marketplace.utilizatori.functii import ui_adauga_un_utilizator, modifica_utilizator_dao, \
    listeaza_toti_utilizatorii, sterge_utilizator


# Create your views here.


def myfunctioncall(request):
    return render(request, "bootstrap_ex/index_ex.html")


def myfunctionabout(request):
    return HttpResponse("ABOUT")


def add(request,a,b):
    return HttpResponse(a+b)


def myfirstpage(request):
    return render(request, "index.html")


def secondpage(request):
    return render(request, 'secondpage.html')


def mythirdpage(request):
    var = "hello world"
    fruits = ["ceva","ceva2"]
    mydictionary = {
        "var": var,
        "myfruits": fruits
    }
    return render(request, 'third.html', context=mydictionary)


def adaugautilizator(request):
    numeUtilizator = request.POST.get('numeUtilizator')
    email = request.POST.get('email')
    detalii = request.POST.get('detalii')

    rezultat = ui_adauga_un_utilizator(numeUtilizator, email, detalii)

    return render(request, 'utilizator_adaugat_cu_success.html')


def modifica_utilizator(request, nume, nume2):
    rezultat = modifica_utilizator_dao(nume, nume2)
    return HttpResponse(rezultat)


def add_nr_crt_to_list(lista):
    counter = 1
    for i in lista:
        i["nr_crt"] = counter
        counter =counter +1


def view_listeaza_toti_utilizatorii(request):
    lista_utilizatori = listeaza_toti_utilizatorii()
    add_nr_crt_to_list(lista_utilizatori)
    d = {
        "lista_utilizatori": lista_utilizatori
    }
    return render(request, 'list_utilizatori.html', context=d)


def listaproduse(request):
    d = listeaza_toate_produsele()
    return render(request, 'list_produse.html', context=d)


def listacomenzi(request):
    d = listeaza_toate_comenzile()
    return render(request, 'list_comenzi.html', context=d)


def signin(request):
    username = request.POST.get('floatingInput')
    password = request.POST.get('floatingPassword')
    if username == "admin@admin" and password == "adminpass":
        return view_listeaza_toti_utilizatorii(request)


    d = {
        "nume": username,
        "password": password,
        "method": request.method
    }
    return JsonResponse(d)

def stergere_utilizator(request):
    nume_de_sters = request.POST.get('numedesters')
    print("nume_de_sters=" + nume_de_sters)
    sterge_utilizator(nume_de_sters)
    return render(request, 'utilizator_sters_cu_success.html')

def contact(request):
    return render(request, 'contact.html')
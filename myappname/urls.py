from django.urls import path
from . import views

urlpatterns =[
    path('', views.myfunctioncall, name="index"),
    path('about', views.myfunctionabout, name="about"),
    path('add/<int:a>/<int:b>', views.add, name="add"),
    path('myfirstpage', views.myfirstpage, name='myfirstpage'),
    path('secondpage', views.secondpage, name='secondpage'),
    path('mythirdpage', views.mythirdpage, name='mythridpage'),
    path('adauga_utilizator', views.adaugautilizator, name="adauga_utilizator"),
    path('modifica_utilizator/<str:nume>/<str:nume2>', views.modifica_utilizator, name="modifica_utilizator"),
    path('listaproduse', views.listaproduse, name="listaproduse"),
    path('listautilizatori', views.view_listeaza_toti_utilizatorii, name="listautilizatori"),
    path('signin', views.signin, name="signin"),
    path('stergere_utilizator', views.stergere_utilizator, name="stergere_utilizator"),
    path('contact', views.contact, name="contact"),
    path('listacomenzi', views.listacomenzi, name="listacomenzi")

]
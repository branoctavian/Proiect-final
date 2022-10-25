import hashlib
import datetime
import json


def genereaza_id_utilizator(nume, email):
    hash_object = hashlib.md5(bytes(nume + email, encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def ui_adauga_un_utilizator(nume, email, detalii):
    if len(nume) not in range(0, 51):
        return "NOK"
    data_inregistrare = str(datetime.datetime.now())
    with open('marketplace.json', "r") as j:
        d = json.load(j)
        utilizator= {
            "nume": nume,
            "email": email,
            "detalii": detalii,
            "data inregistrare": data_inregistrare
        }
        lista_utilizator = d["utilizatori"]

        lista_utilizator.append(utilizator)
        d["utilizatori"] = lista_utilizator

    with open('marketplace.json', "w") as j:
        j.write(json.dumps(d, indent=4))
    return "OK"


def listeaza_toti_utilizatorii():
    with open("marketplace.json", "r") as f:
        d = json.load(f)
        return d["utilizatori"]
        # print(json.dumps(d["utilizatori"], indent=4))


def modifica_utilizator_dao(utilizator_de_modificat, modificare_nume_utilizator):
    data_modificare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        print(json.dumps(d["utilizatori"], indent=4))
        for i in d["utilizatori"]:
            if i["nume"] == utilizator_de_modificat:
                i.update({"nume": modificare_nume_utilizator})
                i.update({"data ultimei modificari": data_modificare})

                with open("marketplace.json", "w") as j:
                    j.write(json.dumps(d, indent=4))
                return "OK"
        else:
            return "NOK"


def modifica_email(utilizator_de_modificat, modificare_email):
    data_modificare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        print(json.dumps(d["utilizatori"], indent=4))
        for i in d["utilizatori"]:
            if d["utilizatori"][i]["nume"] == utilizator_de_modificat:
                d["utilizatori"][i].update({"email": modificare_email})
                d["utilizatori"][i].update({"data ultimei modificari": data_modificare})
                with open("marketplace.json", "w") as j:
                    j.write(json.dumps(d, indent=4))
                return "OK"
        else:
            return "NOK"


def sterge_utilizator(utilizator_de_sters):
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        for i in d["utilizatori"]:
            if i["nume"] == utilizator_de_sters:
                d["utilizatori"].remove(i)
                with open("marketplace.json", "w") as j:
                    j.write(json.dumps(d, indent=4))
                return"OK"
        else:
            return "NOK"


import os

cur_path = os.path.dirname(__file__)
market_place = os.path.relpath('marketplace\\baza_de_date\\marketplace.json', cur_path)



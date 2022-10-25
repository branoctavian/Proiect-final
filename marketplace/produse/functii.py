import hashlib
import json
import datetime


def genereaza_id_produs(nume_produs, cantitate, pret):
    hash_object = hashlib.md5(bytes(nume_produs + str(cantitate) + str(pret), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_produs(nume_produs, pret, cantitate):
    id_produs = str(genereaza_id_produs(nume_produs, cantitate, pret))
    data_inregistrare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        if len(nume_produs) in range(0, 51):
            d["produse"][id_produs] = {
                "nume produs": nume_produs,
                "pret": pret,
                "cantitate": cantitate,
                "data inregistrare": data_inregistrare
            }
            with open("marketplace.json", "w") as j:
                j.write(json.dumps(d, indent=4))
            return "OK"
        else:
            return "NOK"


def listeaza_toate_produsele():
    with open("marketplace.json", "r") as f:
        d = json.load(f)
        return d
        # print(json.dumps(d["produse"], indent=4))


def listeaza_toate_comenzile():
    with open("marketplace.json", "r") as f:
        d = json.load(f)
        return d
        # print(json.dumps(d["produse"], indent=4))


def modificare_nume_produs(produs_de_modificat, modificare_nume_produs):
    data_modificare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        for i in d["produse"]:
            if d["produse"][i]["nume produs"] == produs_de_modificat:
                d["produse"][i].update({"nume produs": modificare_nume_produs})
                d["produse"][i].update({"data ultimei modificari": data_modificare})
                with open("marketplace.json", "w") as j:
                    j.write(json.dumps(d, indent=4))
                return "OK"
        else:
            return "NOK"


def modificare_pret(produs_de_modificat, modificare_pret_produs):
    data_modificare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        for i in d["produse"]:
            if d["produse"][i]["nume produs"] == produs_de_modificat:
                d["produse"][i].update({"pret": modificare_pret_produs})
                d["produse"][i].update({"data ultimei modificari": data_modificare})
                with open("marketplace.json", "w") as j:
                    j.write(json.dumps(d, indent=4))
                return "OK"
        else:
            return "NOK"


def modificare_cantitate(produs_de_modificat, modificare_cantitate_produs):
    data_modificare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        for i in d["produse"]:
            if d["produse"][i]["nume produs"] == produs_de_modificat:
                d["produse"][i].update({"cantitate": modificare_cantitate_produs})
                d["produse"][i].update({"data ultimei modificari": data_modificare})
                with open("marketplace.json", "w") as j:
                    j.write(json.dumps(d, indent=4))
                return "OK"
        else:
            return "NOK"


def sterge_produs(produs_de_sters):
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        for i in d["produse"]:
            if d["produse"][i]["nume produs"] == produs_de_sters:
                del d["produse"][i]
                with open("marketplace.json", "w") as j:
                    j.write(json.dumps(d, indent=4))
                return "OK"
        else:
            return "NOK"
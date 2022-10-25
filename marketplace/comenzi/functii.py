import hashlib
import json
import datetime


def genereaza_id_comanda(data_inregistrare):
    hash_object = hashlib.md5(bytes(json.dumps(data_inregistrare), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_o_comanda(numele_produsului,cantitatea):
    data_inregistrare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        id_comanda = {
            "id_comanda": " ",
            "data_inregistrare": data_inregistrare,
            "detalii_comanda": [],
            "total_plata": 0
        }
        for i in d["produse"]:
            if d["produse"][i]["nume produs"] == numele_produsului:
                id_produs = i
                if d["produse"][i]["cantitate"] > 0:
                    if d["produse"][i]["cantitate"] >= cantitatea:
                        d["produse"][i]["cantitate"] -= cantitatea
                    else:
                        print(f"Stoc insuficient al produsului {numele_produsului}!")
                else:
                    print(f"Stocul produsului {numele_produsului} este epuizat!")
                id_comanda["total_plata"] += cantitatea * d["produse"][i]["pret"]
                id_comanda["detalii_comanda"].append({id_produs: cantitatea})
                idcomanda = str(genereaza_id_comanda(data_inregistrare))
                id_comanda["id_comanda"] = idcomanda
                d["comenzi"][idcomanda] = id_comanda
                with open("marketplace.json", "w") as j:
                    j.write(json.dumps(d, indent=4))
                return"OK"
        else:
            return "NOK"


def adauga_produs(produs_de_adaugat, cantitatea, comanda_de_modificat):
    data_modificare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        for i in d["produse"]:
            if d["produse"][i]["nume produs"] == produs_de_adaugat:
                idProdus = i
                if d["produse"][i]["cantitate"] > 0:
                    if d["produse"][i]["cantitate"] >= cantitatea:
                        d["produse"][i]["cantitate"] -= cantitatea
                    else:
                        return "Stoc epuizat"
                else:
                    print(f"Stocul produsului {produs_de_adaugat} este epuizat!")
                d["comenzi"][comanda_de_modificat]["detalii_comanda"].append({idProdus: cantitatea})
                d["comenzi"][comanda_de_modificat]["total_plata"] += cantitatea * d["produse"][i]["pret"]
                d["comenzi"][comanda_de_modificat].update({"data ultimei modificari": data_modificare})
                return "OK"
        else:
            return "NOK"


def modificare_cantitate(comanda_de_modificat, produs_schimba_cantitatea, noua_cantitate):
    data_modificare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        produse_din_comanda = d["comenzi"][comanda_de_modificat]["detalii_comanda"]
        print(f"Lista produselor din comanda: {produse_din_comanda}")
        for i in range(len(produse_din_comanda)):
            if produs_schimba_cantitatea in produse_din_comanda[i]:
                if noua_cantitate > d["produse"][produs_schimba_cantitatea]["cantitate"]:
                    print(f"Stoc al produsului {produs_schimba_cantitatea} insuficient!")
                    break
                pret = d["produse"][produs_schimba_cantitatea]["pret"]
                diferenta = noua_cantitate - produse_din_comanda[i].get(produs_schimba_cantitatea)
                d["comenzi"][comanda_de_modificat]["total_plata"] += diferenta * pret
                produse_din_comanda[i].update({produs_schimba_cantitatea: noua_cantitate})
                d["produse"][produs_schimba_cantitatea]["cantitate"] -= diferenta
                d["comenzi"][comanda_de_modificat].update({"data ultimei modificari": data_modificare})
                return "OK"
        else:
            return "NOK"


def sterge_produs(comanda_de_modificat, sterge_produs):
    data_modificare = str(datetime.datetime.now())
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        produse_din_comanda = d["comenzi"][comanda_de_modificat]["detalii_comanda"]
        print(f"Lista produselor din comanda: {produse_din_comanda}")
        for i in range(len(produse_din_comanda)):
            if sterge_produs in produse_din_comanda[i]:
                d["comenzi"][comanda_de_modificat].update({"data ultimei modificari": data_modificare})
                pret = d["produse"][sterge_produs]["pret"]
                diferenta = 0 - produse_din_comanda[i].get(sterge_produs)
                d["comenzi"][comanda_de_modificat]["total_plata"] += diferenta * pret
                d["produse"][sterge_produs]["cantitate"] -= diferenta
                del produse_din_comanda[i]
                return "OK"
        else:
            return "NOK"


def listeaza_toate_comenzile():
    with open("marketplace.json", "r") as f:
        d = json.load(f)
        return d
        # print(json.dumps(d["comenzi"], indent=4))


def sterge_o_comanda(comanda_de_sters):
    with open("marketplace.json", "r") as j:
        d = json.load(j)
        chei_comenzi = str(d["comenzi"].keys())
        print(f"Lista comenzilor este: {chei_comenzi}")
        if comanda_de_sters in d["comenzi"]:
            del d["comenzi"][comanda_de_sters]
            with open("marketplace.json", "w") as j:
                j.write(json.dumps(d, indent=4))
            return "OK"
        else:
            return "NOK"
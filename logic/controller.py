class Controller:
    def __init__(self, repo):
        self.repo = repo


    def addClient(self, client):
        self.repo.add(client)

    def sortClient(self):
        return sorted(self.repo.clients)

    def filter_by_id (self, id):
        return list(filter(lambda client: client.id == id, self.repo.clients))

    def filter_by_name(self, partial_name):
        partial_name = partial_name.lower()
        filtered_clients = [client for client in self.repo.clients if partial_name in client.name.lower()]
        return sorted(filtered_clients, key=lambda client: client.name)

    def filter_by_address(self, partial_address):
        partial_address = partial_address.lower()
        filtered_clients = []

        for client in self.repo.clients:
            # Presupunând că obiectul Address are o metodă sau un atribut 'to_string'
            address_str = client.address.to_string().lower() if hasattr(client.address, 'to_string') else str(
                client.address).lower()

            if partial_address in address_str:
                filtered_clients.append(client)

        return sorted(filtered_clients,
                      key=lambda client: client.address.to_string() if hasattr(client.address, 'to_string') else str(
                          client.address))

class MeniuMancare:
    def __init__(self):
        self.meniu = {
            "Pizza": {"pret": 25, "timp": 15},
            "Paste": {"pret": 30, "timp": 10},
            "Steak": {"pret": 50, "timp": 25},
            "Salata": {"pret": 20, "timp": 5}
        }

    def afiseaza_meniu(self):
        print("Meniu:")
        for preparat, detalii in self.meniu.items():
            if isinstance(detalii, dict):
                print(f"{preparat} - {detalii['pret']} RON - Timp de preparare: {detalii['timp']} minute")
            else:
                print(f"Eroare: detaliile pentru '{preparat}' nu sunt în format corect.")

    def adauga_preparat(self, preparat, pret, timp):
        self.meniu[preparat] = {"pret": pret, "timp": timp}
        print(f"{preparat} a fost adăugat cu succes.")

    def scoate_preparat(self, preparat):
        if preparat in self.meniu:
            del self.meniu[preparat]
            print(f"{preparat} a fost scos din meniu.")
        else:
            print(f"{preparat} nu există în meniu.")

    def modifica_pret(self, preparat, pret_nou):
        if preparat in self.meniu:
            self.meniu[preparat]['pret'] = pret_nou
            print(f"Pretul pentru {preparat} a fost modificat.")
        else:
            print(f"{preparat} nu există în meniu.")


class MeniuBautura:
    def __init__(self):
        self.meniu = {
            "Cola": {"pret": 10, "timp": 0, "alcool": 0},
            "Cuba Libre": {"pret": 30, "timp": 5, "alcool": 10},
            "Fanta": {"pret": 10, "timp": 0, "alcool": 0},
            "Apa Minerala": {"pret": 10, "timp": 0, "alcool": 0}
        }

    def afiseaza_meniu(self):
        print("Meniu Bauturi:")
        for preparat, detalii in self.meniu.items():
            if isinstance(detalii, dict):

                mesaj = f"{preparat} - {detalii['pret']} RON"
                if 'timp' in detalii:
                    mesaj += f" - Timp de preparare: {detalii['timp']} minute"
                if 'alcool' in detalii:
                    mesaj += f" - Alcool: {detalii['alcool']}%"
                print(mesaj)
            else:
                print(f"Eroare: detaliile pentru '{preparat}' nu sunt în format corect.")
    def adauga_preparat(self, preparat, pret, timp, alcool):
        self.meniu[preparat] = {"pret": pret, "timp": timp, "alcool": alcool}
        print(f"{preparat} a fost adăugat cu succes.")
    def scoate_preparat(self, preparat):
        if preparat in self.meniu:
            del self.meniu[preparat]
            print(f"{preparat} a fost scos din meniu.")
        else:
            print(f"{preparat} nu există în meniu.")

    def modifica_pret(self, preparat, pret_nou):
        if preparat in self.meniu:
            self.meniu[preparat]['pret'] = pret_nou
            print(f"Pretul pentru {preparat} a fost modificat.")
        else:
            print(f"{preparat} nu există în meniu.")
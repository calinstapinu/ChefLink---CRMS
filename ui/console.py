from logic.controller import *
from entities.client import *
from entities.address import *
from entities.food import *
from repo.repository import *

class Console:
    def __init__(self, controller: Controller):
        self.controller = controller

    def menu(self):
        return """
        Selecteaza o optiune
            1 - Comanda noua
            2 - Setari Meniu
            3 - Filtreaza Clientii dupa Nume/Adresa
            4 - Afiseaza Clientii
            5 - Facturare 
            0 - Exit
        """

    def run(self):
        while True:
            print(self.menu())

            opt = int(input('Optiunea aleasa = '))
            if opt == 0:
                break

            if opt == 1:
                id = int(input('\nId-ul Clientului = '))
                ClientName = input('Numele Clientului = ')
                street = input('Strada Clientului = ')
                number = int(input('Numarul Strazii = '))
                preparat = input('Preparatul Ales = ')
                marime_portie = input('Cantitatea preparatului = ')
                bautura = input('Bautura Aleasa = ')
                alchool = '0%'
                cantitate_bautura= input('Cantitatea bauturii = ')
                pret = random.choice([45, 60, 75, 30])
                datalivrare = int(input('Data livrarii = '))
                oralivrare = input('Ora livrarii ( format HH:MM ) = ')

                client = Client(id, ClientName, Address(street, number), Preparat(preparat, marime_portie), Bautura(bautura, cantitate_bautura, alchool), pret, datalivrare, oralivrare)
                self.controller.addClient(client)

            if opt == 2:
                print('''
                Pe care meniu doresti sa il modifici?
                    1 - Meniu Mancare
                    2 - Meniu Bautura
                ''')

                optiune = int(input('Optiunea Aleasa = '))
                if optiune == 1:
                    meniu = MeniuMancare()
                    while True:
                        print("\na. Afișează meniul")
                        print("b. Adaugă un preparat")
                        print("c. Scoate un preparat")
                        print("d. Modifică prețul unui preparat")
                        print("e. Ieșire")
                        optiune = input("Alege o opțiune: ")

                        if optiune == "a":
                            meniu.afiseaza_meniu()
                        elif optiune == "b":
                            preparat = input("Introduceți numele preparatului: ")
                            pret = int(input("Introduceți prețul: "))
                            timp = int(input("Introduceti timpul de pregatire:"))
                            meniu.adauga_preparat(preparat, pret, timp)
                        elif optiune == "c":
                            preparat = input("Introduceți numele preparatului pe care doriți să-l scoateți: ")
                            meniu.scoate_preparat(preparat)
                        elif optiune == "d":
                            preparat = input("Introduceți numele preparatului pentru care doriți să modificați prețul: ")
                            pret_nou = int(input("Introduceți noul preț: "))
                            meniu.modifica_pret(preparat, pret_nou)
                        elif optiune == "e":
                            break
                        else:
                            print("Opțiune invalidă!")

                if optiune == 2:
                    meniu = MeniuBautura()
                    while True:
                        print("\na. Afișează meniul")
                        print("b. Adaugă un preparat")
                        print("c. Scoate un preparat")
                        print("d. Modifică prețul unui preparat")
                        print("e. Ieșire")
                        optiune = input("Alege o opțiune: ")

                        if optiune == "a":
                            meniu.afiseaza_meniu()
                        elif optiune == "b":
                            preparat = input("Introduceți numele preparatului: ")
                            pret = int(input("Introduceți prețul: "))
                            timp = int(input("Intorduceti timpul de preparare: "))
                            alcool = int(input("Introducet procentajul de alcool "))
                            meniu.adauga_preparat(preparat, pret, timp, alcool)
                        elif optiune == "c":
                            preparat = input("Introduceți numele preparatului pe care doriți să-l scoateți: ")
                            meniu.scoate_preparat(preparat)
                        elif optiune == "d":
                            preparat = input(
                                "Introduceți numele preparatului pentru care doriți să modificați prețul: ")
                            pret_nou = int(input("Introduceți noul preț: "))
                            meniu.modifica_pret(preparat, pret_nou)
                        elif optiune == "e":
                            break
                        else:
                            print("Opțiune invalidă!")

            if opt == 3:
                print('''
                Find by Name or Address?
                    1 - Name
                    2 - Address
                ''')
                optiunefiltrare = int(input('\nOptiunea aleasa= '))

                if optiunefiltrare == 1:
                    name = input('Name: ')
                    clients = self.controller.filter_by_name(name)

                if optiunefiltrare == 2:
                    address = input('Address: ')
                    clients = self.controller.filter_by_address(address)

                for client in clients:
                    print(client)

            if opt == 4:
                clients = self.controller.sortClient()

                for client in clients:
                    print(client)


            if opt == 5:
                name = input('Numele Clientului: ')
                client = self.controller.filter_by_name(name)
                print(client)
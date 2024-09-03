from entities.address import Address
from entities.food import *
from entities.drinks import *
import random

class Client:
    def __init__(self, id: int, name: str, address: Address, preparat: Preparat, bautura: Bautura, pret: int, datalivrare: int, oralivrare: str ):
        self.id = id
        self.name = name
        self.address = address
        self.preparat = preparat
        self.bautura = bautura
        self.pret = pret
        self.datalivrare = datalivrare
        self.oralivrare = oralivrare

    def __str__(self):
        return f'Client(\nId-ul Clientului = {self.id} | Numele Clientului = {self.name} | Adresa Clientului = {self.address} | Preparatul Ales = {self.preparat} | Bautura Aleasa = {self.bautura} | Pretul Final = {self.pret} Ron | Data Livrarii = {self.datalivrare} | Ora Livrarii = {self.oralivrare}\n)'

    def __lt__(self, other):
        return self.name < other.name


    def __eq__(self, other):
        return self.id == other.id

    __repr__ = __str__




class FacturaClient(Client):
    def __init__(self, name: str, address: Address, preparat: Preparat, bautura: Bautura, pret: int):
        self.name = name
        self.address = address
        self.preparat = preparat
        self.bautura = bautura
        self.pret = pret


    def __str__(self):
        return f'Client(\nNumele Clientului = {self.name} \nAdresa Clientului = {self.address} \nPreparatul Ales = {self.preparat} \nBautura Aleasa = {self.bautura} \nPretul Final = {self.pret} Ron\n\n)'

from entities.food import *

class Bautura(Preparat):
    def __init__(self, preparat:str,  marime_portie : str, alchool : str):
        self.preparat=preparat
        self.marime_portie=marime_portie
        self.alchool = alchool


    def __str__(self):
        return f'Bautura(Bautura={self.preparat}, Marime Portie={self.marime_portie}ml, Alchool={self.alchool})'
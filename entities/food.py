
class Preparat:
    def __init__(self, preparat:str,  marime_portie: str):
        self.preparat = preparat
        self.marime_portie = marime_portie


    def __str__(self):
        return f'Mancare(Preparat={self.preparat}, Marime Portie={self.marime_portie}g)'

class TimpGatire(Preparat):
    def __init__(self, marime_portie : str, timpgatire : str):
        super().__init__(Preparat, marime_portie)
        self.timpgatire = timpgatire






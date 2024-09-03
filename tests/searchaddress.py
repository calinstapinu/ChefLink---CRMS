from entities.client import *

class SearchAddress:
    def run(self):
        word = 'come'
        NewList = list(filter(lambda x: word.lower() in x.name.lower() or word.lower() in x.adress.lower()))
        clientaddress = Client(1,'Alexandru', 'COMETEI 22')
        assert NewList[0] == clientaddress
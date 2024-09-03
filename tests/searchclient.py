from entities.client import *


class SearchClient:
    def run(self):
        word = 'ale'
        NewList = list(filter(lambda x: word.lower() in x.name.lower() or word.lower() in x.adress.lower()))
        client = Client(1,'Alexandru', 'Decembrie')
        assert NewList[0] == client
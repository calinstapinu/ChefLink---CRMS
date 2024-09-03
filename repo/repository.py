import pickle

class ClientRepository:
    def __init__(self):
        self.clients = []

    def add(self, client):
        self.clients.append(client)

    def find(self, name):
        for client in self.clients:
            if client.name == name:
                return client

        return None

    def find_i(self, name):
        for client in self.clients:
            if name in client.name:
                return client

        return None

class FileClientRepository(ClientRepository):
    def __init__(self, filename: str):
        super().__init__() #ClientRepository.__init__(self)
        self.filename = filename

    def save(self):
        f = open(self.filename, 'wb')
        pickle.dump(self.clients, f)

        f.close()

    def add(self, client):
        super().add(client)
        self.save()

    def load(self):
        f = open(self.filename, 'rb')
        self.clients = pickle.load(f)
        f.close()

    def to_string(self):
        return list(map(lambda client: pickle.dumps(client), self.clients))

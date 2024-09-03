from logic.controller import *
from entities.client import *
from repo.repository import *

def test_add_client():
    repo = ClientRepository()
    controller = Controller(repo)
    client = Client(1, "Ion Popescu", "Strada Principala", "Pizza", "Cola", "100", "10", "10")
    controller.addClient(client)
    assert client in repo.clients, "Test addClient a eșuat"

def test_sort_client():
    repo = ClientRepository()
    controller = Controller(repo)
    client1 = Client(1, "Ion Popescu", "Strada Principala", "Pizza", "Cola", "100", "10", "10")
    client2 = Client(1, "Ion Popescu", "Strada Principala", "Pizza", "Cola", "100", "10", "10")
    repo.clients = [client2, client1]
    sorted_clients = controller.sortClient()
    assert sorted_clients == [client1, client2], "Test sortClient a eșuat"

def test_filter_by_id():
    repo = ClientRepository()
    controller = Controller(repo)
    client = Client(1, "Ion Popescu", "Strada Principala", "Pizza", "Cola", "100", "10", "10")
    repo.clients = [client]
    result = controller.filter_by_id(1)
    assert result == [client], "Test filter_by_id a eșuat"



# Rularea testelor
test_add_client()
test_sort_client()
test_filter_by_id()

from repo.repository import *
from logic.controller import *
from ui.console import Console


def main():
    print('Alege repositoriul: ( 1 - Memorie | 2 - Fisier )')
    o = int(input('Optiunea aleasa - '))
    r = ClientRepository() if o == 1 else FileClientRepository('clients.dat')

    c = Console(Controller(r))
    # r = StudentRepository()
    # con = Controller(r)
    # c = Console(con)

    c.run()
main()
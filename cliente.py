class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property #fazendo papel do get
    def nome(self):
        print("chamando @property nome() fazendo papel de get") 
        return self.__nome.title() # deixar primeira letra maiuscula (title)

    @nome.setter #fazendo papel do set
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome

from cliente import Cliente    
cliente = Cliente("gabriel")
cliente.nome = "pim"
cliente.nome
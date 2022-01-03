#com orientação objeto

class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto ...{}".format(self))
        self.__numero = numero ## __ equivale a private
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): # metodo privado
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino): # contaOrigem = valor, contaOrigem, contaDestino
        self.saca(valor) # self vai fazer o papel como conta origem para diminuir repetição de codigo
        destino.deposita(valor)

    @property # GET
    def saldo(self):
        return self.__saldo

    @property # GET
    def titular(self):
        return self.__titular

    @property # GET
    def limite(self): # recebe limite GET
        return self.__limite

    @limite.setter #SET
    def limite(self, limite): #modifica o limite SET
        self.__limite = limite

    @staticmethod #metodo estatico não utiliza self
    def codigos_banco():
        bancos = {'BB': '001', 'Caixa':'104','Bradesco':'237'}
        return bancos
    
from conta import Conta      
conta = Conta(123, "gab", 55, 1000)  
conta2 = Conta(1234, "gabb", 70, 1500) 
Conta.codigos_banco()
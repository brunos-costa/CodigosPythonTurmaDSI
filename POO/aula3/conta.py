class Conta:
    def __init__(self,numero,titular,saldo,limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

        self.__limite = limite
    
    def depositar(self,valor):
        if valor < 0:
            print("Você não pode despositar valor negativo")
        else:
            self.__saldo += valor

    def sacar(self,valor):
        if valor > self.__saldo:
            print(f"Você não pode sacar este valor, seu saldo é {self.__saldo}")
        else:
            self.__saldo -= valor
    
    def getSaldo(self):
        print(f"Seu saldo é {self.__saldo}")


# Outra forma de criar getters e setters
class Conta2:
    def __init__(self,numero,titular,saldo,limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

        self.__limite = limite
    
    #decorator
    # Exibir o saldo
    @property
    def saldo(self):
        return f"O seu saldo é R$ {self.__saldo}"
    
    # Inserir valores no atributo
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Você não pode depositar valores negativos")
        else:
            self.__saldo += valor
            print("Valor depositado com sucesso")
        





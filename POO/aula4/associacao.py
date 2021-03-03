
class Celular:
    def __init__(self,marca,valor):
        self.__marca = marca
        self.__valor = valor    
    @property
    def marca(self):
        return self.__marca    
    @property
    def valor(self):
        return self.__valor
class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco

        # Atributo que vai estar relacionado com a classe celular
        self.__celular = None

    @property
    def nome(self):
        return str(self.__nome).title()

    @property
    def idade(self):
        if self.__idade < 0:
            self.__idade *= -1
        return self.__idade
    
    @property
    def endereco(self):
        return str(self.__endereco).lower()
    
    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self,valor):
        self.__celular = valor
         
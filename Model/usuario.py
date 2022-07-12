from Model.pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self,nome,cpf,senha,genero,idade,contaBancaria):
        super().__init__(nome,cpf,senha,genero,idade)
        self.contaBancaria = contaBancaria

    def getContaBancaria(self):
        return self.contaBancaria

    def setContaBancaria(self,contaBancaria):
        self.contaBancaria = contaBancaria
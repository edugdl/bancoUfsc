from Model.pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome, cpf, senha, genero, idade):
        super().__init__(nome, cpf, senha, genero, idade)
        self.contaBancaria = []

    def getListaContaBancaria(self):
        return self.contaBancaria

    def setContaBancaria(self, contaBancaria):
        self.contaBancaria = contaBancaria

    def adicionarContaBancaria(self, contaBancaria):
        self.contaBancaria.append(contaBancaria)

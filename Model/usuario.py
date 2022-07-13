from Model.pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome, cpf, senha, genero, idade, salario):
        super().__init__(nome, cpf, senha, genero, idade)
        self.contaBancaria = []
        self.salario = salario

    def getListaContaBancaria(self):
        return self.contaBancaria

    def setListaContaBancaria(self, contaBancaria):
        self.contaBancaria = contaBancaria

    def adicionarContaBancaria(self, contaBancaria):
        self.contaBancaria.append(contaBancaria)

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario = salario
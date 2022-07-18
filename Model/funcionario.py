from Model.pessoa import Pessoa
from View.telaAdmin import telaAdmin
from View.telaFuncionario import telaFuncionario


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, senha, genero, idade, permissao):
        super().__init__(nome, cpf, senha, genero, idade)
        self.permissao = permissao

    def abrirTela(self, listaFuncionarios, listaPessoas):
        if self.getPermissao() == 'S':
            acesso = int(
                input('1-Administrador\n2-Funcionário\nInsira como deseja acessar: '))
            if acesso == 1:
                telaAdmin.tela(self, listaFuncionarios)
            elif acesso == 2:
                telaFuncionario.tela(self, listaPessoas)
        else:
            telaFuncionario.tela(self, listaPessoas)

    def getPermissao(self):
        return self.permissao

    def setPermissao(self, permissao):
        self.permissao = permissao

from Model.pessoa import Pessoa
from Model.usuario import Usuario
from View.telaFuncionario import telaFuncionario

class Funcionario(Pessoa):
    def __init__(self,nome,cpf,senha,genero,idade,permissao):
        super().__init__(nome,cpf,senha,genero,idade)
        self.permissao = permissao

    def abrirTela(self,listaPessoas):
        telaFuncionario.tela(self,listaPessoas)

    def getPermissao(self):
        return self.permissao

    def setPermissao(self,permissao):
        self.permisso = permissao
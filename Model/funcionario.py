from Model.pessoa import Pessoa
from Model.usuario import Usuario
from View.telaFuncionario import telaFuncionario

class Funcionario(Pessoa):
    def __init__(self,nome,cpf,senha,genero,idade):
        super().__init__(nome,cpf,senha,genero,idade)

    def abrirTela(self,listaPessoas):
        telaFuncionario.tela(self,listaPessoas)
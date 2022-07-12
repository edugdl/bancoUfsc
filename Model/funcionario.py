from Model.pessoa import Pessoa
from Model.usuario import Usuario
from View.telaFuncionario import telaFuncionario

class Funcionario(Pessoa):
    def __init__(self,nome,cpf,senha,genero,idade,listaPessoas):
        super().__init__(nome,cpf,senha,genero,idade)
        self.listaPessoas = listaPessoas
        
    def getListaPessoas(self):
        return self.listaPessoas
    
    def setListaPessoas(self,listaPessoas):
        self.listaPessoas = listaPessoas

    def abrirTela(self,listaPessoas):
        telaFuncionario.tela(self,listaPessoas)
        
    def cadastrarUsuario(self,nome,cpf,senha,genero,idade,contaBancaria):
        pessoaCriada = Usuario(nome,cpf,senha,genero,idade,contaBancaria)
        return pessoaCriada
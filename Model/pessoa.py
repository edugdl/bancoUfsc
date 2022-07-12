from View.telaUsuario import telaUsuario

class Pessoa:
    def __init__(self, nome, cpf, senha, genero, idade):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.genero = genero
        self.idade = idade

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCpf(self):
        return self.cpf

    def setCpf(self, cpf):
        self.cpf = cpf

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero
    
    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

    def abrirTela(self,listaPessoas):
        telaUsuario.tela(self,listaPessoas)
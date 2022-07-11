from pessoa import *
from contaBancaria import *

def existeUsuarioCadastrado(cpf,senha,listaPessoas):
    for pessoa in listaPessoas:
        if pessoa.cpf == cpf and pessoa.senha == senha:
            print(f'Olá {pessoa.nome}')
            return pessoa
    else:
        print('Cpf e/ou senha incorretos!')
        return False
    
listaPessoas = list()
conta = contaBancaria(4500.00,'Premium',None)
eduardo = Usuario('Eduardo','a','1','M', 17,conta)
manuella = Funcionario('Manuella','b','2','F',17,listaPessoas)
print('Olá, Bem-Vindo(a) ao Banco')
listaPessoas.append(eduardo)
listaPessoas.append(manuella)

def main():
    while True:
        print('1 - Login')
        print('2 - Sair')
        acao = int(input('O que deseja fazer? '))
        if acao == 1:
            cpf = input('Insira seu cpf: ')
            senha = input('Insira sua senha: ')
            login = existeUsuarioCadastrado(cpf,senha,listaPessoas)
            while not login:
                print('Caso queira sair insira o cpf como 0')
                cpf = input('Insira novamente seu cpf: ')
                if cpf == '0':
                    break
                senha = input('Insira novamente sua senha: ')
                login = existeUsuarioCadastrado(cpf, senha, listaPessoas)
            if cpf != '0':
                login.abrirTela()
        else:
            break
if __name__  == '__main__':
    main()
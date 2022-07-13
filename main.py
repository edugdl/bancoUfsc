from Model.contaBancaria import contaPoupanca, contaBancaria
from Model.usuario import Usuario
from Model.funcionario import Funcionario


def existeUsuarioCadastrado(cpf, senha, listaGeral):
    for pessoa in listaGeral:
        if pessoa.cpf == cpf and pessoa.senha == senha:
            print(f'Olá {pessoa.nome}')
            return pessoa
    else:
        print('Cpf e/ou senha incorretos!')
        return False


listaPessoas = list()
listaGeral = list()
conta = contaBancaria(4500.00, 'conta1')
conta2 = contaBancaria(0, 'conta2')
conta3 = contaPoupanca(1000, 'testePoupanca')
conta4 = contaPoupanca(2000, "micaelGostosoRendeDinheiro")
eduardo = Usuario('Eduardo', 'a', '1', 'M', 18, 1000)
eduardo.adicionarContaBancaria(conta)
eduardo.adicionarContaBancaria(conta3)
micael = Usuario('Micael', 'c', '3', 'M', 20, 2000)
micael.adicionarContaBancaria(conta2)
micael.adicionarContaBancaria(conta4)
manuella = Funcionario('Manuella', 'b', '2', 'F', 18)
print('Olá, Bem-vindo(a) ao Banco')
listaGeral.append(eduardo)
listaGeral.append(manuella)
listaGeral.append(micael)
listaPessoas.append(eduardo)
listaPessoas.append(micael)


def main():
    while True:
        print('1 - Login')
        print('2 - Sair')
        acao = int(input('O que deseja fazer? '))
        if acao == 1:
            cpf = input('Insira seu cpf: ')
            senha = input('Insira sua senha: ')
            login = existeUsuarioCadastrado(cpf, senha, listaGeral)
            while not login:
                print('Caso queira sair insira o cpf como 0')
                cpf = input('Insira novamente seu cpf: ')
                if cpf == '0':
                    break
                senha = input('Insira novamente sua senha: ')
                login = existeUsuarioCadastrado(cpf, senha, listaGeral)
            if cpf != '0':
                login.abrirTela(listaPessoas)
        elif acao == 2:
            break


if __name__ == '__main__':
    main()
